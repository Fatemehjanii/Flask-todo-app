from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate


# --- Flask Setup ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app)
migrate = Migrate(app, db)


# --- SQLAlchemy Model ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {'id': self.id, 'task': self.task, 'done': self.done}

# --- Admin Interface ---
admin = Admin(app, name='MyAdmin', template_mode='bootstrap3')
admin.add_view(ModelView(Task, db.session))

"""# --- Database creation ---
with app.app_context():
    db.create_all()"""

# --- Routes ---

@app.route('/')
def hello():
    # مثال خواندن کوکی
    username = request.cookies.get('username', 'Guest')
    tasks = Task.query.all()
    return render_template('hello.html', tasks=tasks, username=username)

# --- API Routes ---
@app.route("/api/to_do", methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/to_do/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())

@app.route('/api/to_do/done', methods=['GET'])
def get_done_tasks():
    tasks = Task.query.filter_by(done=True).all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/to_do', methods=['POST'])
def add_task():
    data = request.get_json() if request.is_json else request.form
    task_name = data.get('task')
    done = data.get('done', False) in [True, 'true', 'on']

    new_task = Task(task=task_name, done=done)
    db.session.add(new_task)
    db.session.commit()

    socketio.emit('update', {'action':'add', 'task': new_task.to_dict()}, broadcast=True)
    return jsonify(new_task.to_dict()), 201

@app.route('/api/to_do/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.task = data.get('task', task.task)
    task.done = data.get('done', task.done)
    db.session.commit()

    socketio.emit('update', {'action':'update', 'task': task.to_dict()}, broadcast=True)
    return jsonify(task.to_dict())

@app.route('/api/to_do/<int:id>', methods=['PATCH'])
def patch_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    if 'task' in data: task.task = data['task']
    if 'done' in data: task.done = data['done']
    db.session.commit()

    socketio.emit('update', {'action':'update', 'task': task.to_dict()}, broadcast=True)
    return jsonify(task.to_dict())

@app.route('/api/to_do/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    socketio.emit('update', {'action':'delete', 'id': id}, broadcast=True)
    return jsonify({'message':'Task deleted'})

# --- Cookies Example ---
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie has been set!")
    resp.set_cookie('username', 'Fatemeh')
    return resp

# --- AJAX Example (فرم ارسال بدون Refresh) ---
@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    task_name = request.form.get('task')
    new_task = Task(task=task_name, done=False)
    db.session.add(new_task)
    db.session.commit()

    socketio.emit('update', {'action':'add', 'task': new_task.to_dict()}, broadcast=True)
    return jsonify(new_task.to_dict())

# --- HEAD request ---
@app.route('/api/to_do', methods=['HEAD'])
def head_tasks():
    return '', 200

# --- SocketIO Events ---
@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

# --- Run Server ---
if __name__ == '__main__':
    socketio.run(app, debug=True)

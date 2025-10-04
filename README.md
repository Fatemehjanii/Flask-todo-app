# Flask To-Do App 📝

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Build](https://github.com/Fatemehjanii/Flask-todo-app/actions/workflows/python-app.yml/badge.svg)](https://github.com/Fatemehjanii/Flask-todo-app/actions/workflows/python-app.yml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#)

A **professional To-Do application** built with Flask, featuring **task management, AJAX, SocketIO, Flask-Admin, SQLAlchemy, and a modern responsive UI**.

---

## ✨ Features

### 🖥 Frontend
- ✅ Task list with **Done / Pending** status and color indicators  
- ⚡ Add tasks dynamically **without page refresh** using **AJAX**  
- 🌐 **Real-time updates** across clients with **SocketIO**  
- 🎨 **Modern, responsive UI** with clean styling  

### 🛠 Backend
- 🛠️ Task management through **Flask-Admin dashboard**  
- 🗄️ Database integration with **SQLAlchemy**  

### 👋 Extras
- 👋 Welcome banner using **Cookies**  


---


## 📸 Screenshots

![Main Page](./static/screenshot_home.png)  
![Admin Panel](./static/screenshot_admin.png)  

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Fatemehjanii/Flask-todo-app.git
   cd Flask-todo-app
2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   flask run
   ```
   The app will be available at:  
   👉 `http://127.0.0.1:5000`

---

## 📂 Project Structure

```
flask-todo-app/
│
├── app.py                # Main application
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignored files for Git
├── static/               # Static files (CSS, JS, images)
│   └── style.css
├── templates/            # HTML templates
│   └── index.html
└── migrations/           # Database migrations (if using Flask-Migrate)
```

---

## 🔥 Tech Stack

- ![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) **Flask** – Python microframework for backend development  
- ![SocketIO](https://img.shields.io/badge/Socket.IO-FF652F?logo=socket.io) **Flask-SocketIO** – Real-time communication between server & clients  
- ![Admin](https://img.shields.io/badge/Flask-Admin-6DB33F?logo=flask) **Flask-Admin** – Admin panel for easy database management  
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-000000?logo=sqlalchemy) **SQLAlchemy** – Object-Relational Mapping (ORM) for database  
- ![JavaScript](https://img.shields.io/badge/AJAX-JS-yellow?logo=javascript) **AJAX / JavaScript** – Dynamic front-end interactions without page refresh  
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5) + ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3) **Modern UI** – Responsive and clean styling

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it for your own projects. 🚀  
َ
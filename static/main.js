const socket = io();

const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');

function createTaskElement(task) {
    const li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between align-items-center';
    li.dataset.id = task.id;

    const span = document.createElement('span');
    span.textContent = task.task;
    if(task.done) span.classList.add('text-decoration-line-through', 'text-muted');

    const div = document.createElement('div');

    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'btn btn-success btn-sm toggleBtn me-1';
    toggleBtn.textContent = task.done ? 'Undo' : 'Done';
    toggleBtn.onclick = () => toggleTask(task.id);

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'btn btn-danger btn-sm deleteBtn';
    deleteBtn.textContent = 'Delete';
    deleteBtn.onclick = () => deleteTask(task.id);

    div.appendChild(toggleBtn);
    div.appendChild(deleteBtn);

    li.appendChild(span);
    li.appendChild(div);

    return li;
}

function addTask() {
    const task = taskInput.value.trim();
    if(!task) return;
    fetch('/api/tasks', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({task})
    });
    taskInput.value = '';
}

function toggleTask(id) {
    fetch(`/api/tasks/${id}`, {method: 'PUT'});
}

function deleteTask(id) {
    fetch(`/api/tasks/${id}`, {method: 'DELETE'});
}

addBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', e => { if(e.key==='Enter') addTask(); });

socket.on('update', data => {
    if(data.action==='add') {
        taskList.appendChild(createTaskElement(data.task));
    } else if(data.action==='update') {
        const li = taskList.querySelector(`[data-id='${data.task.id}']`);
        li.replaceWith(createTaskElement(data.task));
    } else if(data.action==='delete') {
        const li = taskList.querySelector(`[data-id='${data.id}']`);
        if(li) li.remove();
    }
});

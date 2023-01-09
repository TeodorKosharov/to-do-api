const ipv4Address = '3.83.24.165:8000';

window.onload = populateTasksList;

function customAlert(icon, title, text, html) {
    if (html) Swal.fire({
        icon, title, html
    }); else Swal.fire({
        icon, title, text
    });
}

async function handleAddTaskForm() {
    event.preventDefault();
    const formData = new FormData(event.target);
    const name = formData.get('name');
    const difficulty = formData.get('difficulty');
    const priority = formData.get('priority');
    event.target.reset();

    const response = await fetch(`http://${ipv4Address}/create-task/`, {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
            name, difficulty, priority
        })
    });
    const message = await response.json();

    if (message === 'Task created successfully!') {
        customAlert('success', 'Success', message);
        await populateTasksList();
    } else {
        customAlert('error', 'Oops...', message);
    }
}

async function handleDetailsForm() {
    event.preventDefault();
    const taskNameInput = document.getElementById('task-name');
    const result = await (await fetch(`http://${ipv4Address}/details/${taskNameInput.value}/`)).json();
    taskNameInput.value = '';

    if (typeof result === 'string') customAlert('error', 'Oops...', 'There is no task with such name!'); else customAlert('success', 'Task found', undefined, `<div>Name: ${result.name}</div>    
             <div>Difficulty: ${result.difficulty}</div>    
             <div>Priority: ${result.priority}</div>`);
}

async function handleEditForm() {
    event.preventDefault();

    const formData = new FormData(event.target);
    const currentName = formData.get('name');
    const name = formData.get('new-name');
    const difficulty = formData.get('new-difficulty');
    const priority = formData.get('new-priority');
    event.target.reset();

    const response = await fetch(`http://${ipv4Address}/edit-task/${name}/`, {
        method: 'PUT', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
            currentName, name, difficulty, priority
        })
    });
    const message = await response.json();
    if (message === 'Task updated!') {
        customAlert('success', 'Success', message);
        await populateTasksList();
    } else {
        customAlert('error', 'Oops...', message);
    }
}

async function handleDeleteForm() {
    event.preventDefault();

    const taskNameInput = document.getElementById('delete-task-name');
    const response = await fetch(`http://${ipv4Address}/delete-task/${taskNameInput.value}/`, {
        method: 'DELETE', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
            "taskName": taskNameInput.value
        })
    });
    taskNameInput.value = '';
    const message = await response.json();
    if (message === 'There is no task with such name!') {
        customAlert('error', 'Oops...', message);
    } else {
        customAlert('success', 'Success', message);
        await populateTasksList();
    }
}

async function populateTasksList() {
    const tasks = await (await fetch(`http://${ipv4Address}/tasks/`)).json();
    const tasksList = document.getElementById('tasks-list');
    tasksList.textContent = '';
    if (tasks.length) {
        tasks.forEach(task => {
            const taskListEl = document.createElement('li');
            taskListEl.textContent = task.name;
            tasksList.append(taskListEl);
        });
    } else {
        const noTasksEl = document.createElement('li');
        noTasksEl.textContent = 'No available tasks';
        tasksList.append(noTasksEl);
    }
}

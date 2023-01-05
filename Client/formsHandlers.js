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

    const response = await fetch('http://127.0.0.1:8000/create-task/', {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
            name, difficulty, priority
        })
    });
    const responseMessage = await response.json();

    if (typeof responseMessage === 'object') {
        const errorMessage = responseMessage.name[0];
        customAlert('error', 'Error', errorMessage[0].toUpperCase() + errorMessage.slice(1));
    } else {
        customAlert('success', 'Success', responseMessage);
        await populateTasksList();
    }
}

async function handleDetailsForm() {
    event.preventDefault();
    const taskNameInput = document.getElementById('task-name');
    const result = await (await fetch(`http://127.0.0.1:8000/details/${taskNameInput.value}/`)).json();
    taskNameInput.value = '';

    if (typeof result === 'string') customAlert('error', 'Oops...', 'There is no task with such name!'); else customAlert('success', 'Task found', undefined, `<div>Name: ${result.name}</div>    
             <div>Difficulty: ${result.difficulty}</div>    
             <div>Priority: ${result.priority}</div>`);
}

async function populateTasksList() {
    const tasks = await (await fetch('http://127.0.0.1:8000/tasks/')).json();
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

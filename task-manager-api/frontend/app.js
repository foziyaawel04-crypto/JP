const API_URL = 'http://localhost:5000/api/tasks';

const taskForm = document.getElementById('taskForm');
const titleInput = document.getElementById('titleInput');
const priorityInput = document.getElementById('priorityInput');
const taskList = document.getElementById('taskList');
const priorityFilter = document.getElementById('priorityFilter');
async function fetchTasks() {
  const priority = priorityFilter ? priorityFilter.value : 'all';
  let url = API_URL;
  
  if (priority && priority !== 'all') {
    url += `?priority=${priority}`;
  }

  try {
    const res = await fetch(url);
    const tasks = await res.json();
    renderTasks(tasks);
  } catch (err) {
    console.error('Error fetching tasks:', err);
  }
}

function renderTasks(tasks) {
  taskList.innerHTML = '';
  
  tasks.forEach(task => {
    const taskId = task._id || task.id; 
    
    const li = document.createElement('li');
    li.className = 'task-item';
    
    li.innerHTML = `
      <div class="task-content">
        <input 
          type="checkbox" 
          ${task.completed ? 'checked' : ''} 
          onchange="toggleTask('${taskId}', ${!task.completed})"
        >
        <span class="task-title ${task.completed ? 'completed' : ''}">${task.title}</span>
        <span class="badge ${task.priority}">${task.priority}</span>
      </div>
      <button class="btn-delete" onclick="deleteTask('${taskId}')">Delete</button>
    `;
    
    taskList.appendChild(li);
  });
}
taskForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const title = titleInput.value.trim();
  const priority = priorityInput.value;

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, priority })
    });

    if (res.ok) {
      titleInput.value = '';
      fetchTasks();
    }
  } catch (err) {
    console.error('Error adding task:', err);
  }
});
async function toggleTask(id, completed) {
  try {
    await fetch(`${API_URL}/${id}`, {
      method: 'PATCH', // or PUT depending on backend
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed })
    });
    fetchTasks();
  } catch (err) {
    console.error('Error updating task:', err);
  }
}

async function deleteTask(id) {
  try {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
    fetchTasks();
  } catch (err) {
    console.error('Error deleting task:', err);
  }
}

if (priorityFilter) {
  priorityFilter.addEventListener('change', fetchTasks);
}

fetchTasks();
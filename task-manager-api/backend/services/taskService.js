let tasks = require('../data/taskData');

let nextId = 5;

const getAllTasks = (priority, completed) => {
  let result = [...tasks];
  
  if (priority) {
    result = result.filter(t => t.priority.toLowerCase() === priority.toLowerCase());
  }
  
  if (completed !== undefined) {
    const isCompleted = completed === 'true';
    result = result.filter(t => t.completed === isCompleted);
  }
  
  return result;
};

const getTaskById = (id) => {
  return tasks.find(t => t.id === parseInt(id));
};

const createTask = ({ title, priority }) => {
  const newTask = {
    id: nextId++,
    title,
    completed: false,
    priority
  };
  tasks.push(newTask);
  return newTask;
};

const updateTask = (id, updates) => {
  const index = tasks.findIndex(t => t.id === parseInt(id));
  if (index === -1) return null;

  tasks[index] = { ...tasks[index], ...updates, id: parseInt(id) };
  return tasks[index];
};

const deleteTask = (id) => {
  const index = tasks.findIndex(t => t.id === parseInt(id));
  if (index === -1) return false;

  tasks.splice(index, 1);
  return true;
};

module.exports = {
  getAllTasks,
  getTaskById,
  createTask,
  updateTask,
  deleteTask
};
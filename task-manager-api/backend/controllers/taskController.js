const taskService = require('../services/taskService');

const getTasks = (req, res) => {
  const { priority, completed } = req.query;
  const tasks = taskService.getAllTasks(priority, completed);
  res.status(200).json(tasks);
};

const getTaskById = (req, res) => {
  const task = taskService.getTaskById(req.params.id);
  if (!task) {
    return res.status(404).json({ error: `Task with id ${req.params.id} not found` });
  }
  res.status(200).json(task);
};

const createTask = (req, res) => {
  const { title, priority } = req.body;

  if (!title || typeof title !== 'string' || title.trim() === '') {
    return res.status(400).json({ error: "Title is required and must be a non-empty string." });
  }

  const validPriorities = ['low', 'medium', 'high'];
  if (!priority || !validPriorities.includes(priority.toLowerCase())) {
    return res.status(400).json({ error: "Priority must be one of: low, medium, high." });
  }

  const newTask = taskService.createTask({
    title: title.trim(),
    priority: priority.toLowerCase()
  });

  res.status(201).json(newTask);
};

const updateTask = (req, res) => {
  const { title, priority, completed } = req.body;

  if (priority) {
    const validPriorities = ['low', 'medium', 'high'];
    if (!validPriorities.includes(priority.toLowerCase())) {
      return res.status(400).json({ error: "Priority must be one of: low, medium, high." });
    }
  }

  const updatedTask = taskService.updateTask(req.params.id, {
    ...(title && { title: title.trim() }),
    ...(priority && { priority: priority.toLowerCase() }),
    ...(completed !== undefined && { completed: Boolean(completed) })
  });

  if (!updatedTask) {
    return res.status(404).json({ error: `Task with id ${req.params.id} not found` });
  }

  res.status(200).json(updatedTask);
};

const deleteTask = (req, res) => {
  const success = taskService.deleteTask(req.params.id);
  if (!success) {
    return res.status(404).json({ error: `Task with id ${req.params.id} not found` });
  }
  res.status(200).json({ message: "Task deleted successfully" });
};

module.exports = {
  getTasks,
  getTaskById,
  createTask,
  updateTask,
  deleteTask
};
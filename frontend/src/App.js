import React, { useState, useEffect } from "react";
import axios from "axios";

const App = () => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  const fetchTasks = async () => {
    const response = await axios.get("http://localhost:5000/todos");
    setTasks(response.data);
  };

  const addTask = async () => {
    await axios.post("http://localhost:5000/todos", { title: newTask });
    setNewTask("");
    fetchTasks();
  };

  const toggleTask = async (id, completed) => {
    await axios.put(`http://localhost:5000/todos/${id}`, { completed: !completed });
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await axios.delete(`http://localhost:5000/todos/${id}`);
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="p-4 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold text-center mb-4">Taskology</h1>
      <div className="flex justify-center mb-4">
        <input
          className="p-2 border rounded-l"
          placeholder="Add a task"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
        />
        <button
          className="p-2 bg-blue-500 text-white rounded-r"
          onClick={addTask}
        >
          Add
        </button>
      </div>
      <div className="flex">
        <div className="w-1/2 p-2">
          <h2 className="text-2xl font-semibold">To-Do</h2>
          {tasks.filter((task) => !task.completed).map((task) => (
            <div key={task.id} className="flex justify-between items-center p-2 border-b">
              <span>{task.title}</span>
              <div>
                <button
                  className="text-green-500 mr-2"
                  onClick={() => toggleTask(task.id, task.completed)}
                >
                  Complete
                </button>
                <button className="text-red-500" onClick={() => deleteTask(task.id)}>
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
        <div className="w-1/2 p-2">
          <h2 className="text-2xl font-semibold">Completed Tasks</h2>
          {tasks.filter((task) => task.completed).map((task) => (
            <div key={task.id} className="flex justify-between items-center p-2 border-b">
              <span>{task.title}</span>
              <div>
                <button
                  className="text-yellow-500 mr-2"
                  onClick={() => toggleTask(task.id, task.completed)}
                >
                  Undo
                </button>
                <button className="text-red-500" onClick={() => deleteTask(task.id)}>
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;


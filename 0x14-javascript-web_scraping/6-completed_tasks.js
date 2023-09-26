#!/usr/bin/node
// Computes the number of tasks completed by user id.

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }

  const todos = JSON.parse(body);

  const completedTasks = todos.filter((todo) => todo.completed);

  const userTasks = {};
  for (const todo of completedTasks) {
    if (!userTasks[todo.userId]) {
      userTasks[todo.userId] = 1;
    } else {
      userTasks[todo.userId]++;
    }
  }
  console.log(userTasks);
});

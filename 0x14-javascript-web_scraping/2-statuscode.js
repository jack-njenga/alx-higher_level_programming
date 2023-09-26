#!/usr/bin/node
// Displays the status code of a GET request.

const args = process.argv;
const request = require('request');

request.get(args[2], (error, response) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});

#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    console.log('Content saved');
  });
});

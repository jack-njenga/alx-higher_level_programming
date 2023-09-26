#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  fs.writeFile(path, body, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
});

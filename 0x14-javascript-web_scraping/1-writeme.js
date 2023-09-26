#!/usr/bin/node
// Writes a string to a file.

const args = process.argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});

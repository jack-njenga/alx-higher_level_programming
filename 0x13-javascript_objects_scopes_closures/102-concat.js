#!/usr/bin/node

const fs = require('fs');
const path = require('path');

if (process.argv.length > 4) {
  const path1 = path.resolve(process.argv[2]);
  const path2 = path.resolve(process.argv[3]);
  const saveas = path.resolve(process.argv[4]);

  try {
    const file1 = fs.readFileSync(path1, 'utf8');
    const file2 = fs.readFileSync(path2, 'utf8');
    const filec = file1 + file2;

    fs.writeFileSync(saveas, filec, 'utf8');
  } catch (error) {
    console.error(error.message);
  }
}

#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (arg) {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let n = 0; n < arg; n++) {
      row = row + 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

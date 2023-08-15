#!/usr/bin/node

const fs = require('fs');

const path1 = process.argv[2];
const path2 = process.argv[3];
const saveas = process.argv[4];

const file1 = fs.readFileSync(path1, 'utf8');
const file2 = fs.readFileSync(path2, 'utf8');
const filec = file1 + file2;

fs.writeFileSync(saveas, filec, 'utf8');

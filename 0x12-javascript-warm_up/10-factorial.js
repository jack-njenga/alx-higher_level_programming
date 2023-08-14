#!/usr/bin/node
const args = process.argv;

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 2) {
    return 2;
  }
  return (n * factorial(n - 1));
}

console.log(factorial(parseInt(args[2])));

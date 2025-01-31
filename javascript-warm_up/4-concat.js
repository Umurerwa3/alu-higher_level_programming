#!/usr/bin/node
const arg1 = process.argv[2]; // First argument
const arg2 = process.argv[3]; // Second argument

if (arg1 && arg2) {
  console.log(arg1 + ' is ' + arg2);
} else if (arg1) {
  console.log(arg1);
}

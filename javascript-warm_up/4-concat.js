#!/usr/bin/node
const arg1 = process.argv[2]; // First argument (if any)
const arg2 = process.argv[3]; // Second argument (if any)

if (arg1 !== undefined && arg2 !== undefined) {
  console.log(arg1 + ' is ' + arg2);
} else if (arg1 !== undefined) {
  console.log(arg1);
}
// If no arguments, it prints nothing (which is correct).

#!/usr/bin/node
const arg = process.argv[2]; // First argument
const num = parseInt(arg, 10); // Convert to an integer

if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}

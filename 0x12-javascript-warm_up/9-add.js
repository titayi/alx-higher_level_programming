#!/usr/bin/node

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(firstInt, secondInt));

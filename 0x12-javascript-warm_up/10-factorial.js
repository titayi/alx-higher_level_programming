#!/usr/bin/node

function factorial (t) {
  if (isNaN(t) || t === 0) {
    return 1;
  } else {
    return t * factorial(t - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));

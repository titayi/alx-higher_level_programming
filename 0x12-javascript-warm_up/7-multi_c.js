#!/usr/bin/node

const cIsFun = parseInt(process.argv[2]);
if (isNaN(cIsFun)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < cIsFun; i++) {
    console.log('C is fun');
  }
}

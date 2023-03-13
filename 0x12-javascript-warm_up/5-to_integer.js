#!/usr/bin/node

const convertArgc = parseInt(process.argv[2]);
if (isNaN(convertArgc)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertArgc);
}

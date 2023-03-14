#!/usr/bin/node

const list = require('./101-data').dict;

const newDict = {};

Object.keys(list).forEach(key => {
  if (newDict[list[key]] === undefined) newDict[list[key]] = [];
  newDict[list[key]].push(key);
});
console.log(newDict);

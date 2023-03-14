#!/usr/bin/node

const SquareModel = require('./5-square');

class Square extends SquareModel {
  charPrint (c) {
    const charC = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(charC.repeat(this.width));
    }
  }
}

module.exports = Square;

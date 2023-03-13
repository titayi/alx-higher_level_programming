#!/usr/bin/node

module.exports = {
  addMeMaybe: function (m, t) {
    return t(m + 1);
  }
};

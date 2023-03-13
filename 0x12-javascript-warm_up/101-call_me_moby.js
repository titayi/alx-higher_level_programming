#!/usr/bin/node

module.exports = {
  callMeMoby: function (m, t) {
    for (let i = 0; i < m; i++) {
      t();
    }
  }
};

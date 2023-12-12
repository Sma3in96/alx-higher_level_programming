#!/usr/bin/node
exports.callMeMoby = function (n, b) {
  for (let i = 0; i < n; i++) {
    b();
  }
};

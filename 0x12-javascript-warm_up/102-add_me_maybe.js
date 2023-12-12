#!/usr/bin/node
exports.addMeMaybe = function (n, func) {
  n = parseInt(n) + 1;
  func(n);
};

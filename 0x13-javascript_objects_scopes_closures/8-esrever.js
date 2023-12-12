#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length;
  for (let i = 0; i < size / 2; i++) {
    let temp = list[i];
    list[i] = list[- 1 - i];
    list[- 1 - i] = temp; 
  }
};

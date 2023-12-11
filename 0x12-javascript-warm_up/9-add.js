#!/usr/bin/node
function add(a, b) {
  return a + b;
}
const list = process.argv.slice(2);
console.log(add(parseInt(list[0]), parseInt(list[1])));

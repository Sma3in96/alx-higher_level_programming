#!/usr/bin/node
const list = process.argv.slice(2);
let x = parseInt(list[0]);
function fact(n) {
  if (n == 0 || isNaN(n)) {
    return 1;
  }
  return fact(n - 1) * n;
}
console.log(fact(x));

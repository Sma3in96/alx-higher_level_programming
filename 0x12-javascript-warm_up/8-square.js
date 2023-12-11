#!/usr/bin/node
const list = process.argv.slice(2);
const n = parseInt(list[0]);
if (n) {
  for (let i = 0; i < n; i++) {
    let str1 = '';
    for (let j = 0; j < n; j++) {
      str1 += 'X';
    }
    console.log(str1);
  }
}

#!/usr/bin/node
const list = process.argv.slice(2);
let str1, str2;
if (list[0] && list[1]) {
  str1 = list[0];
  str2 = list[1];
} else if (list[0]) {
  str1 = list[0];
}
console.log(str1 + ' is ' + str2);

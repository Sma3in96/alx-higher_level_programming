#!/usr/bin/node
const list = process.argv.slice(2);
if (list.length < 2) {
  console.log(0);
} else {
  let big = 0; let big2nd = 0;
  for (let i = 0; i < list.length; i++) {
    if (parseInt(list[i]) > big) {
      big2nd = big;
      big = parseInt(list[i]);
    } else if (parseInt(list[i]) < big && parseInt(list[i]) > big2nd) {
      big2nd = parseInt(list[i]);
    } else {
      continue;
    }
  }
  console.log(big2nd);
}

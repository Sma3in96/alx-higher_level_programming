#!/usr/bin/node
const list = process.argv.slice(2);
if (list[0]) {
  let x = parseInt(list[0]);
  if (x) {
    console.log(x);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}

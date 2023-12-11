#!/usr/bin/node
const list = process.argv.slice(2);
const x = parseInt(list[0]);
if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

#!/usr/bin/node
const args = process.argv.slice(2);
let x = args[0]; let y;
if (isNaN(x)) { console.log('Missing size'); }
if (x > 0) {
  y = x;
  while (x--) {
    console.log('X'.repeat(y));
  }
}

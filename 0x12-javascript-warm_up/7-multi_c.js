#!/usr/bin/node
const args = process.argv.slice(2);
let x = args[0];
if (isNaN(x)) { console.log('Missing number of occurrences'); }
while (x--) {
  console.log('C is fun');
}

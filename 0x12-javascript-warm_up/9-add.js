#!/usr/bin/node
const args = process.argv.slice(2);
const x = Number(args[0]); const y = Number(args[1]);
if (isNaN(args[0]) && isNaN(args[1])) {
  console.log('NaN');
} else {
  console.log(x + y);
}

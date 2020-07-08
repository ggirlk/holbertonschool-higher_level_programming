#!/usr/bin/node
const args = process.argv.slice(2);
let x = Number(args[0]); let y = Number(args[1]);
if (isNaN(x) && isNaN(y)) { console.log('NaN'); }
if (x && y) {
    console.log(x + y);
} else { console.log('NaN'); }

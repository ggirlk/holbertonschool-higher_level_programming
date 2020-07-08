#!/usr/bin/node
// Concat files
const args = process.argv.slice(2);
const fs = require('fs');
let str1 = fs.readFileSync(args[0]);
let str2 = fs.readFileSync(args[1]);
fs.appendFile(args[2], str1.concat(str2).trim());
fs.appendFile(args[2], '\n');

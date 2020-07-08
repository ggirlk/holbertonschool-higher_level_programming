#!/usr/bin/node
// Sorted occurences
const dict = require('./101-data').dict;
const a = {};
for (const i in dict) {
  if (a[dict[i]] === undefined) {
    a[dict[i]] = [];
  }
  a[dict[i]].push(i);
}
console.log(a);

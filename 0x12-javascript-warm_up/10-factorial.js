#!/usr/bin/node
const args = process.argv.slice(2);
const x = Number(args[0]);
function Factorial (n) {
  let k = 1;
  for (let i = 2; i <= n; i++) { k = k * i; }
  return k;
}
console.log(Factorial(x));

#!/usr/bin/node
let args = process.argv.slice(2);
let str = '';
if (args[0])
{
str += args[0];
} else {
str += "undefined";
}
str += " is ";
if (args[1])
{
str += args[1];
} else {
str += "undefined";
}
console.log(str);

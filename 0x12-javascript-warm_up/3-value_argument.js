#!/usr/bin/node
// Arguments
let i = 0;
let str = "";
process.argv.forEach((val, index) => {
  if (i > 1) {
    if (`${val}`) {
      str += `${val} `;
    }
  }
  i++;
});
if (i === 2) {
  console.log('No argument');
} else {
  console.log(str);
}

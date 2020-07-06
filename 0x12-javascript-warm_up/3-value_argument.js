#!/usr/bin/node
// Arguments
let i = 0;
process.argv.forEach((val, index) => {
  if (i > 1) {
    if (`${val}`) {
      console.log(`${val}`);
    }
  }
  i++;
});
if (i === 2) {
  console.log('No argument');
}

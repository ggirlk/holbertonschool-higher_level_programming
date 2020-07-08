#!/usr/bin/node
// Log me
let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};

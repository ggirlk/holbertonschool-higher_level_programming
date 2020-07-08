#!/usr/bin/node
// Number conversion
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};

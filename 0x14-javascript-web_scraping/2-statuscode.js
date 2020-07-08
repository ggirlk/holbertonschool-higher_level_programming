#!/usr/bin/node
// Status code
require('request').get(process.argv[2], function (err, r) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + r.statusCode);
  }
});

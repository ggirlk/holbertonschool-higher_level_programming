#!/usr/bin/node
// Star wars movie title
require('request').get('http://swapi.co/api/films/' + process.argv[2] + '/', function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});

#!/usr/bin/node
const request = require('request');
url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + process.argv[2], (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});

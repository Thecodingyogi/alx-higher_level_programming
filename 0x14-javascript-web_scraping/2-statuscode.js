#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (error, response) => {
  console.log(error || `code: ${response.statusCode}`);
});

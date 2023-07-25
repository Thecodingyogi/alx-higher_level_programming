#!/usr/bin/node
const request = require('request');
const characterId = 18;
const API_URL = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    const moviesWithWedgeAntilles = results.filter((film) =>
      film.characters.includes(API_URL));
    console.log(`${moviesWithWedgeAntilles.length}`);
  }
});

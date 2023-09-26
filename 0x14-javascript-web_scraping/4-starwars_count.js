#!/usr/bin/node
// Prints the number of movies where the character
// “Wedge Antilles” is present.

const args = process.argv;
const request = require('request');

const url = `${args[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }
  const data = JSON.parse(body);
  const countMovies = data.results.filter((film) => {
    return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
  });

  console.log(countMovies.length);
});

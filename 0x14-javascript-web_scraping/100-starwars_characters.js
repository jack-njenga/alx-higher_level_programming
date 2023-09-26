#!/usr/bin/node
// Prints all characters of a Star Wars movie.

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const urls = data.characters;

  const characterData = (url) => {
    request.get(url, (err, response, body) => {
      if (err) {
        process.exit(1);
      }
      const charData = JSON.parse(body);
      console.log(charData.name);

      if (urls.length > 0) {
        const nextUrl = urls.shift();
        characterData(nextUrl);
      }
    });
  };
  if (urls.length > 0) {
    const firstUrl = urls.shift();
    characterData(firstUrl);
  }
});

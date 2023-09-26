#!/usr/bin/node
// Prints the title of a Star Wars movie where the
// episode number matches a given integer.

const args = process.argv;
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const bodyData = JSON.parse(body);
  console.log(bodyData.title);
});

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const movies = JSON.parse(body).results;
    let number = 0;
    for (const index in movies) {
      const cast = movies[index].characters;
      for (const ind in cast) {
        if (cast[ind] == 'https://swapi-api.alx-tools.com/api/people/18/') {
          number++;
        }
      }
    }
    console.log(number);
  }
});

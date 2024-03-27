#!/usr/bin/node

const request = require('request');
const ID = 18;
const url = process.argv[2].replace('films', 'people') + '/' +ID;


request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});

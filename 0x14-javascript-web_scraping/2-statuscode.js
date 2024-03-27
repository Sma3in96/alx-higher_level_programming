#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, reply) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code: ', reply.statusCode);
});

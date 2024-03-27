#!/usr/bin/node
const request = require('request')
const url = process.argv[1]

request(url, (error, reply) => {
  if (error) {
    console.error(error);
  }
  console.log(reply.statusCode)
})

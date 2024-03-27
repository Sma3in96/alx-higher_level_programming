#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const tasks = JSON.parse(body);
    const dict = {};
    for (let i = 1; i <= 10; i++) {
      dict[i] = 0;
    }
    for (const task in tasks) {
      if (tasks[task].completed === true) {
        const index = tasks[task].userId;
        dict[index]++;
      }
    }
    console.log(dict);
  }
});

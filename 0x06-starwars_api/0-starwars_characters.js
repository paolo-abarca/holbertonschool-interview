#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2] + '/';

request.get(url + id, async function (error, response, body) {
  if (error) {
    return console.error(error);
  }

  const jsonbody = JSON.parse(body).characters;
  for (const character of jsonbody) {
    await new Promise(function (resolve, reject) {
      request.get(character, function (error, response, body) {
        if (error) {
          return console.error(error);
        }

        const jsonbody = JSON.parse(body);
        console.log(jsonbody.name);
        resolve();
      });
    });
  }
});

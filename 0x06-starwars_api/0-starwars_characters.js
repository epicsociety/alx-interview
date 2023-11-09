#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const charactersUrls = JSON.parse(body).characters;
  const fetchCharacterPromises = [];

  charactersUrls.forEach((character) => {
    const fetchPromise = new Promise((resolve, reject) => {
      request.get(character, function (error, response, body) {
        if (error) {
          console.error(error);
          return;
        }

        const characterName = JSON.parse(body).name;
        resolve(characterName);
      });
    });
    fetchCharacterPromises.push(fetchPromise);
  });

  Promise.all(fetchCharacterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.erro(error);
    });
});

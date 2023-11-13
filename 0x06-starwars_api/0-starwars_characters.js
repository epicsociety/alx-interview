#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(filmID);

// #!/usr/bin/node

// const request = require('request');
// const movieId = process.argv[2];
// const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// request.get(url, function (error, response, body) {
//   if (error) {
//     console.error(error);
//     return;
//   }
//   const charactersUrls = JSON.parse(body).characters;
//   const fetchCharacterPromises = [];

//   charactersUrls.forEach((character) => {
//     const fetchPromise = new Promise((resolve, reject) => {
//       request.get(character, function (error, response, body) {
//         if (error) {
//           console.error(error);
//           return;
//         }

//         const characterName = JSON.parse(body).name;
//         resolve(characterName);
//       });
//     });
//     fetchCharacterPromises.push(fetchPromise);
//   });

//   Promise.all(fetchCharacterPromises)
//     .then((characterNames) => {
//       characterNames.forEach((name) => {
//         console.log(name);
//       });
//     })
//     .catch((error) => {
//       console.erro(error);
//     });
// });

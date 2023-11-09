#!/usr/bin/node

const request = require('request');

const getCharacters = async () => {
    try {
        const movieId = process.argv[2];
        const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
        
        const response = await promisifiedRequest(apiUrl);
        const charsUrl = JSON.parse(response).characters;

        for (const url of charsUrl) {
            const characterResponse = await promisifiedRequest(url);
            const characterName = JSON.parse(characterResponse).name;
            console.log(characterName);
        }
    } catch (error) {
        consoler.error(error);
    }
};


const promisifiedRequest = (url) => {
    return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                resolve(body);
            }
        });
    });
}

getCharacters();

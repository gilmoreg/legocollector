'use strict';
const jwt = require('jsonwebtoken');
const nodeFetch = require('node-fetch');

module.exports.update = (event, context, callback) => {
  nodeFetch(`${process.env.API_URL}/legoset/update`, {
    method: 'POST',
    body: JSON.stringify({
      token: jwt.sign(process.env.ADMIN, process.env.SECRET)
    }),
  })
  .then(res => res.json())
  .then((message) => {
    console.log(message);
    const response = {
      statusCode: 200,
      body: JSON.stringify({ message }),
    };
    return callback(null, response);
  })
  .catch((message) => {
    console.error(message);
    return callback(message, null);
  });
};

/* eslint-disable import/prefer-default-export */
export const API_URL = process.env.NODE_ENV === 'production' ?
  'https://legocollector.herokuapp.com' :
  'http://localhost:5000';

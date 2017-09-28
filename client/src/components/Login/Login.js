import React from 'react';
import './Login.css';

// TODO move to config/env
const API_URL = 'http://localhost:5000';

const storeProfile = (accessToken, email) => {
  window.localStorage.setItem(
    'legocollectorProfile',
    JSON.stringify({ accessToken, email }),
  );
};

const fetchProfile = accessToken =>
  fetch(`${API_URL}/login`,
    { method: 'POST',
      body: JSON.stringify({ access_token: accessToken }),
    })
    .then(res => res.json())
    .then(res => storeProfile(res.token, res.email));

const amazonLogin = () =>
  window.amazon.Login.authorize({ scope: 'profile' },
    response => fetchProfile(response.access_token));

export default () => (
  <button id="LoginWithAmazon" onClick={amazonLogin}>
    <img
      alt="Login with Amazon"
      src="https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png"
      width="156"
      height="32"
    />
  </button>
);

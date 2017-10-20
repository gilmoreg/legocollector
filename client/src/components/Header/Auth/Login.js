import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { login, fetchWatches } from '../../../state/actions';
import './Login.css';

// TODO move to config/env
const API_URL = 'http://localhost:5000';

const storeProfile = ({ token, email }) => {
  console.log('storeProfile', token, email);
  window.localStorage.setItem(
    'legocollectorProfile',
    JSON.stringify({ token, email }),
  );
};

const fetchProfile = accessToken =>
  fetch(`${API_URL}/login`,
    { method: 'POST',
      body: JSON.stringify({ access_token: accessToken }),
    })
    .then(res => res.json())
    .then(res => res.result);

export class Login extends Component {
  constructor(props) {
    super(props);
    this.amazonLogin = this.amazonLogin.bind(this);
  }

  amazonLogin() {
    window.amazon.Login.authorize({ scope: 'profile' },
      response =>
        fetchProfile(response.access_token)
          .then((profile) => {
            storeProfile(profile);
            this.props.dispatch(login(profile));
            this.props.dispatch(fetchWatches(profile.token));
          }));
  }

  render() {
    return (
      <button id="LoginWithAmazon" onClick={this.amazonLogin}>
        <img
          alt="Login with Amazon"
          src="https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png"
          width="156"
          height="32"
        />
      </button>
    );
  }
}

Login.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

export default connect()(Login);

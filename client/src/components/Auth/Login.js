import React, { Component } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import { connect } from 'react-redux';
import { login, fetchWatches } from '../../state/actions';
import { API_URL } from '../../config';

const StyledButton = styled.button`
  border: none;
  background-color: transparent;
`;

export class Login extends Component {
  constructor(props) {
    super(props);
    this.storeProfile = this.storeProfile.bind(this);
    this.fetchProfile = this.fetchProfile.bind(this);
    this.amazonLogin = this.amazonLogin.bind(this);
  }

  storeProfile({ token, email }) {
    try {
      window.localStorage.setItem(
        'legocollectorProfile',
        JSON.stringify({ token, email }),
      );
    } catch (e) {
      console.error(e);
    }
  };

  fetchProfile(accessToken) {
    return fetch(`${API_URL}/login`,
      { method: 'POST',
        body: JSON.stringify({ access_token: accessToken }),
      })
      .then(res => res.json())
      .then(res => res.result);
  }

  amazonLogin() {
    return window.amazon.Login.authorize({ scope: 'profile' },
      response =>
        this.fetchProfile(response.access_token)
          .then((profile) => {
            this.storeProfile(profile);
            this.props.dispatch(login(profile));
            this.props.dispatch(fetchWatches(profile.token));
          })
          .catch(error => console.error(error)),
      error => console.error(error));
  }

  render() {
    return (
      <StyledButton id="LoginWithAmazon" onClick={this.amazonLogin}>
        <img
          alt="Login with Amazon"
          src="https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png"
          width="156"
          height="32"
        />
      </StyledButton>
    );
  }
}

Login.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

export default connect()(Login);

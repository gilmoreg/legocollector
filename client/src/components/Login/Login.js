import React, { Component } from 'react';

export default class Login extends Component {
  constructor(props) {
    super(props);
    this.login = this.login.bind(this);
  }

  login() {
    window.amazon.Login.authorize(
      { scope: 'profile' },
      'https://www.example.com/handle_login.php');
    return this;
  }

  render() {
    return (
      <a href id="LoginWithAmazon" onClick={this.login}>
        <img
          border="0"
          alt="Login with Amazon"
          src="https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png"
          width="156"
          height="32"
        />
      </a>
    );
  }
}

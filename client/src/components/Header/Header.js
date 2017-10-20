import React from 'react';
import PropTypes from 'prop-types';
import Login from './Auth/Login';
import './Header.css';

const Header = props => (
  <header className="Header">
    <h1>Lego Collector Tools</h1>
    { props.loggedIn ?
      <span>Logged in as {props.email}</span> :
      <Login />
    }
  </header>
);

Header.defaultProps = {
  email: '',
  loggedIn: false,
};

Header.propTypes = {
  email: PropTypes.string,
  loggedIn: PropTypes.bool,
};

export default Header;

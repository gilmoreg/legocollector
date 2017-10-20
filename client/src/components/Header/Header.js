import React from 'react';
import PropTypes from 'prop-types';
import Login from './Auth/Login';
import Logout from './Auth/Logout';
import './Header.css';

const Header = props => (
  <header className="Header">
    <h1>Lego Collector</h1>
    { props.loggedIn ?
      <Logout /> :
      <Login />
    }
  </header>
);

Header.defaultProps = {
  loggedIn: false,
};

Header.propTypes = {
  loggedIn: PropTypes.bool,
};

export default Header;

import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import Login from '../Auth/Login';
import Logout from '../Auth/Logout';

const StyledHeader = styled.header`
  background: radial-gradient(ellipse at center, rgba(62,69,76,1) 0%,rgba(27,50,73,1));
  padding: 1rem;
`;

const StyledH1 = styled.h1`
  font-family: 'Roboto Slab', 'Courier New', Courier, monospace;
  color: #FF7F66;
  margin: 0.25rem;
`;

const Header = props => (
  <StyledHeader className="Header">
    <StyledH1>Lego Collector</StyledH1>
    { props.loggedIn ?
      <Logout /> :
      <Login />
    }
  </StyledHeader>
);

Header.defaultProps = {
  loggedIn: false,
};

Header.propTypes = {
  loggedIn: PropTypes.bool,
};

export default Header;

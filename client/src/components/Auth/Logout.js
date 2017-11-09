import React, { Component } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import { connect } from 'react-redux';
import { logout } from '../../state/actions';

const StyledDiv = styled.div`
  padding: 0.25rem;
`;

const StyledSpan = styled.span`
  color: #2185C5;
`;

const StyledButton = styled.button`
  display: block;
  background-color: #FF7F66;
  border: none;
  border-radius: 5px;
  margin: 0.5rem auto 0 auto;
  font-size: 12px;
`;

export class Logout extends Component {
  constructor(props) {
    super(props);
    this.logout = this.logout.bind(this);
  }

  logout() {
    window.localStorage.removeItem('legocollectorProfile');
    this.props.dispatch(logout());
  }

  render() {
    return (
      <StyledDiv>
        <StyledSpan>Logged in as {this.props.email}</StyledSpan>
        <StyledButton onClick={this.logout}>Logout</StyledButton>
      </StyledDiv>
    );
  }
}

Logout.defaultProps = {
  email: '',
};

Logout.propTypes = {
  email: PropTypes.string,
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  email: state.email,
});

export default connect(mapStateToProps)(Logout);

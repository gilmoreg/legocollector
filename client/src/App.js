import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Login from './components/Login/Login';
import { login, logout } from './state/actions';
import './App.css';

const checkProfile = () => {
  const profile = JSON.parse(
    window.localStorage.getItem('legocollectorProfile'));
  console.log(profile);
  if (profile && profile.email && profile.token) return profile;
  return null;
};

class App extends Component {
  componentWillMount() {
    // Check for stored profile and set login state accordingly
    const profile = checkProfile();
    if (profile) this.props.dispatch(login(profile));
    else this.props.dispatch(logout);
  }

  render() {
    return (
      <div className="App">
        { this.props.loggedIn ?
          <span>Logged in as {this.props.email}</span> :
          <Login /> }
      </div>
    );
  }
}

App.propTypes = {
  dispatch: PropTypes.func.isRequired,
  loggedIn: PropTypes.bool,
  email: PropTypes.string,
};

App.defaultProps = {
  loggedIn: false,
  email: '',
};

const mapStateToProps = state => ({
  loggedIn: state.loggedIn,
  email: state.email,
});

export default connect(mapStateToProps)(App);

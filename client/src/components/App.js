import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { login, logout } from '../state/actions';
import Login from './Login/Login';
import Watch from './Watch/Watch';
import './App.css';

const checkProfile = () => {
  const profile = JSON.parse(
    window.localStorage.getItem('legocollectorProfile'));
  if (profile && profile.email && profile.token) return profile;
  return null;
};

const fakeWatch = {
  title: 'LEGO Ideas NASA Apollo Saturn V 21309 Building Kit',
  image: 'https://images-na.ssl-images-amazon.com/images/I/413yqVUgjcL._SL160_.jpg',
  url: 'https://www.amazon.com/LEGO-Ideas-Apollo-Saturn-Building/dp/B01MUANC80?psc=1&SubscriptionId=AKIAJ57KMBTCZPRJ5I5Q&tag=gilmoreg-20&linkCode=xm2&camp=2025&creative=165953&creativeASIN=B01MUANC80',
  currentStock: 1000,
}

export class App extends Component {
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
        <Watch watch={fakeWatch} />
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

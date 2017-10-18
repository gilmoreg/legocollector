import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { login, logout, fetchWatches } from '../state/actions';
import Login from './Login/Login';
import Watch from './Watch/Watch';
import AddWatchButton from './AddWatch/AddWatchButton';
import AddWatchModal from './AddWatch/AddWatchModal';
import './App.css';

const checkProfile = () => {
  const profile = JSON.parse(
    window.localStorage.getItem('legocollectorProfile'));
  if (profile && profile.email && profile.token) return profile;
  return null;
};

export class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      newWatchModalOpen: false,
    };
  }


  componentWillMount() {
    // Check for stored profile and set login state accordingly
    const profile = checkProfile();
    if (profile) {
      this.props.dispatch(login(profile));
      this.props.dispatch(fetchWatches(profile.token));
    } else this.props.dispatch(logout);
  }

  render() {
    const watches = this.props.watches.map(watch =>
      <Watch watch={watch} key={watch.id} />);

    return (
      <div className="App">
        { this.props.loggedIn ?
          <span>Logged in as {this.props.email}</span> :
          <Login /> }
        {watches}
        <AddWatchButton
          openModal={() => this.setState({ newWatchModalOpen: !this.state.newWatchModalOpen })}
        />
        { this.state.newWatchModalOpen ?
          <AddWatchModal
            open={this.state.newWatchModalOpen}
            close={() => this.setState({ newWatchModalOpen: false })}
          /> : ''
        }
      </div>
    );
  }
}

App.propTypes = {
  dispatch: PropTypes.func.isRequired,
  loggedIn: PropTypes.bool,
  email: PropTypes.string,
  watches: PropTypes.array,
};

App.defaultProps = {
  loggedIn: false,
  email: '',
  watches: [],
};

const mapStateToProps = state => ({
  loggedIn: state.loggedIn,
  email: state.email,
  watches: state.watches,
});

export default connect(mapStateToProps)(App);

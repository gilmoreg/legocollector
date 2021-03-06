import React, { Component } from 'react';
import PropTypes from 'prop-types';
import styled, { keyframes } from 'styled-components';
import { connect } from 'react-redux';
import { login, logout, fetchWatches, openModal } from '../state/actions';
import { API_URL } from '../config';
import Header from './Header/Header';
import Welcome from './Welcome/Welcome';
import Watch from './Watch/Watch';
import AddWatchButton from './AddWatch/AddWatchButton';
import Instructions from './Welcome/Instructions';

const StyledApp = styled.div`
  text-align: center;
  min-height: 100%;
`;

const StyledWatchView = styled.div`
  margin-bottom: 7rem;
`;

const loadingKeyframes = keyframes`
  0% {
    max-width: 0;
  }
`;

const AnimatedH2 = styled.h2`
  &:before {
    content: attr(data-text);
    position: absolute;
    overflow: hidden;
    max-width: 20em;
    white-space: nowrap;
    color: #2185C5;
    animation: ${loadingKeyframes} 8s linear;
  }
`;

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
      serverAwake: false,
      serverError: '',
    };
  }

  componentDidMount() {
    // Check for stored profile and set login state accordingly
    const profile = checkProfile();
    if (profile) {
      this.props.dispatch(login(profile));
      this.props.dispatch(fetchWatches(profile.token));
    } else this.props.dispatch(logout);
    // Keep the user notified of progress waking the server up
    fetch(`${API_URL}/`)
      .then(() => this.setState({ serverAwake: true }))
      .catch(() => this.setState({ serverError: 'Sorry, we couldn\'t contact the server.' }));
  }

  render() {
    const watches = this.props.watches.map(watch =>
      <Watch watch={watch} key={watch.id} />);

    return (
      <div className="App">
        <StyledApp>
          <Header loggedIn={this.props.loggedIn} email={this.props.email} />
          { this.props.loggedIn ?
            <StyledWatchView>
              { this.state.serverAwake ? '' : <AnimatedH2 data-text="Please wait while we gather your sets...">Please wait while we gather your sets...</AnimatedH2>}
              { this.state.serverError ? <h2>{this.state.serverError}</h2> : ''}
              { watches.length ? watches : <Instructions /> }
            </StyledWatchView>
            :
            <Welcome />
          }
          { this.props.loggedIn ?
            <AddWatchButton
              openModal={() => this.props.dispatch(openModal())}
            /> :
            ''
          }
        </StyledApp>
      </div>
    );
  }
}

App.propTypes = {
  dispatch: PropTypes.func.isRequired,
  loggedIn: PropTypes.bool,
  email: PropTypes.string,
  watches: PropTypes.array,
  className: PropTypes.string,
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

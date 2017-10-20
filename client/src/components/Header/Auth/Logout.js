import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { logout } from '../../../state/actions';
import './Logout.css';

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
      <div className="Logout">
        <span>Logged in as {this.props.email}</span>
        <button onClick={this.logout}>Logout</button>
      </div>
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

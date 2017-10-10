/* eslint-disable jsx-a11y/no-static-element-interactions */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import './AddWatchModal.css';

export class AddWatchModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      setID: '',
    };
    this.submitForm = this.submitForm.bind(this);
  }

  submitForm(event) {
    console.log(event, this.state);
  }

  render() {
    return (
      <div className="AddWatchModal" onClick={this.props.closeModal}>
        <form onSubmit={this.submitForm}>
          <input onChange={val => this.setState({ setID: val })} />
        </form>
      </div>
    );
  }
}

AddWatchModal.defaultProps = {
  dispatch: () => {},
};

AddWatchModal.propTypes = {
  closeModal: PropTypes.func.isRequired,
  dispatch: PropTypes.func,
};

export default connect()(AddWatchModal);

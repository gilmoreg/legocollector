import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import './AddWatchModal.css';

export class AddWatchModal extends Component {
  constructor(props) {
    super(props);
    this.state = {

    }
    this.submitForm = this.submitForm.bind(this);
  }

  submitForm(event) {
    console.log(event, this.state);
  }

  render() {
    return (
      <div className="AddWatchModal">
        <form onSubmit={this.submitForm}>
          <input />
        </form>
      </div>
    );
  }
}

AddWatchModal.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

export default connect()(AddWatchModal);

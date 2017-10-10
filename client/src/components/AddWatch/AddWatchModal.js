/* eslint-disable jsx-a11y/no-static-element-interactions */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactModal from 'react-modal';
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
      <ReactModal
        isOpen={this.props.open}
        contentLabel="Add New Watch"
        overlayClassName="Overlay"
        className="AddWatchModal"
        shouldCloseOnOverlayClick
        onRequestClose={this.props.close}
        role="dialog"
        parentSelector={() => document.querySelector('#root')}
      >
        <form onSubmit={this.submitForm}>
          Lego ID: <input onChange={val => this.setState({ setID: val })} />
        </form>
      </ReactModal>
    );
  }
}

AddWatchModal.defaultProps = {
  parent: <div />,
  open: false,
  close: () => {},
  dispatch: () => {},
};

AddWatchModal.propTypes = {
  parent: PropTypes.func,
  open: PropTypes.bool,
  close: PropTypes.func,
  dispatch: PropTypes.func,
};

export default connect()(AddWatchModal);

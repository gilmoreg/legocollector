/* eslint-disable jsx-a11y/no-static-element-interactions */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactModal from 'react-modal';
import { connect } from 'react-redux';
import throttle from 'lodash.throttle';
import { API_URL } from '../../config';
import './AddWatchModal.css';

export class AddWatchModal extends Component {
  constructor(props) {
    super(props);
    this.submitForm = this.submitForm.bind(this);
    this.state = {
      searchResult: {},
    };
    this.search = throttle((event) => {
      fetch(`${API_URL}/legoset/search/${event.target.value}?token=${this.props.token}`)
        .then(res => res.json())
        .then((res) => {
          if (res && res.result) this.setState({ searchResult: res.result });
        })
        .catch(err => console.error(err)); // TODO proper error message
    }, 250);
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
          Lego ID:
          <input
            type="text"
            onChange={this.search}
          />
        </form>
      </ReactModal>
    );
  }
}

AddWatchModal.defaultProps = {
  token: '',
  open: false,
  close: () => {},
  dispatch: () => {},
};

AddWatchModal.propTypes = {
  token: PropTypes.string,
  open: PropTypes.bool,
  close: PropTypes.func,
  dispatch: PropTypes.func,
};

const mapStateToProps = props => ({
  token: props.token,
});

export default connect(mapStateToProps)(AddWatchModal);

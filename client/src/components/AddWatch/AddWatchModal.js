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
      searchTerm: '',
      searchResult: {},
    };
    this.search = throttle(query => this.queryAPI(query), 250);
    this.onInputChange = this.onInputChange.bind(this);
    this.queryAPI = this.queryAPI.bind(this);
  }

  onInputChange(event) {
    event.persist();
    if (event.target && event.target.value) {
      const query = event.target.value.trim();
      this.setState({ searchTerm: query });
      this.search(query);
    }
  }

  queryAPI(query) {
    fetch(`${API_URL}/legoset/search/${query}?token=${this.props.token}`)
      .then(res => res.json())
      .then((res) => {
        if (res && res.result) this.setState({ searchResult: res.result });
        console.log(res.result);
      })
      .catch(err => console.error(err)); // TODO proper error message
  }

  submitForm(event) {
    event.preventDefault();
    this.search();
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
            onChange={this.onInputChange}
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
  // dispatch: PropTypes.func,
};

const mapStateToProps = props => ({
  token: props.token,
});

export default connect(mapStateToProps)(AddWatchModal);

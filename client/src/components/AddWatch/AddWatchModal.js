/* eslint-disable jsx-a11y/no-static-element-interactions */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Modal from 'react-modal';
import { connect } from 'react-redux';
import debounce from 'lodash.debounce';
import { API_URL } from '../../config';
import Examples from './Examples';
import SearchResult from './SearchResult';
import { addWatch } from '../../state/actions';
import './AddWatchModal.css';

// Only digits, and between 1 and 7 of them (valid input)
const digitTest = RegExp(/^\d{1,7}$/);
// Only digits, and between 5 and 7 of them (valid API query)
const digitLengthTest = RegExp(/^\d{5,7}$/)

export class AddWatchModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchTerm: '',
      searchResult: {},
      error: '',
    };
    this.search = debounce(() => this.queryAPI(), 250);
    this.setSearchTerm = this.setSearchTerm.bind(this);
    this.onInputChange = this.onInputChange.bind(this);
    this.submitForm = this.submitForm.bind(this);
    this.queryAPI = this.queryAPI.bind(this);
    this.addWatch = this.addWatch.bind(this);
    this.displayError = this.displayError.bind(this);
    this.input = { value: '' };
  }

  setSearchTerm(event) {
    const id = event.target.dataset.id;
    this.setState({ searchTerm: id });
  }

  onInputChange(event) {
    event.persist();
    if (event.target && event.target.value) {
      const query = event.target.value.trim();
      if (query.match(digitTest)) this.setSearchTerm(query);
      if (query) this.search();
    }
  }

  submitForm(event) {
    event.preventDefault();
    this.search();
  }

  queryAPI() {
    const query = this.state.searchTerm;
    if (!query || !query.match(digitLengthTest)) {
      this.displayError('Set ID must be a 5 to 7 digit number!');
      return;
    }
    fetch(`${API_URL}/legoset/search/${query}?token=${this.props.token}`)
      .then(res => res.json())
      .then((res) => {
        if (!res) return this.displayError('Something went wrong');
        if (res.result) this.setState({ searchResult: res.result });
        if (res.error) this.displayError(res.error);
      })
      .catch(err => this.displayError(err));
  }

  addWatch() {
    if (this.state.searchResult.id) {
      fetch(`${API_URL}/watches/add`, {
        method: 'POST',
        body: JSON.stringify({
          id: this.state.searchResult.id,
          token: this.props.token,
        }),
      })
        .then(res => res.json())
        .then((res) => {
          if (res.result) {
            this.props.dispatch(addWatch(res.result));
            this.props.close();
          }
          if (res.error) {
            this.displayError(res.error);
          }
        })
        .catch(err => this.displayError(err));
    }
  }

  displayError(err) {
    let error;
    if (typeof err === 'object') {
      // If we didn't get any response, the API is probably down
      if (!err) error = 'Error communicating with the server. Please try again later.';
      else error = JSON.stringify(err);
    } else error = err;
    this.setState({ error });
    // Clear error after 5 seconds
    setTimeout(() => {
      this.setState({ error: '' });
    }, 5000);
  }
 
 render() {
   return (
    <Modal
      isOpen={this.props.open}
      contentLabel="Add New Watch"
      overlayClassName="Overlay"
      className="AddWatchModal"
      shouldCloseOnOverlayClick
      onRequestClose={this.props.close}
      role="dialog"
      parentSelector={() => document.querySelector('.App')}
    >
      <div className="AddWatchModalContent">
        <form onSubmit={this.submitForm}>
          <h3>Lego ID:</h3>
          <Examples click={this.setSearchTerm} />
          <input
            type="text"
            placeholder={75105}
            onChange={this.onInputChange}
            value={this.state.searchTerm}
          />
          { this.state.error ? <small>{this.state.error}</small> : ''}
        </form>
        {this.state.searchResult.id ?
          <SearchResult
            legoset={this.state.searchResult}
            onClick={this.addWatch}
          />
        : ''}
      </div>
    </Modal>
  );
 }
}

AddWatchModal.defaultProps = {
  open: false,
  close: () => {},
  dispatch: () => {},
};

AddWatchModal.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  dispatch: PropTypes.func,
};

const mapStateToProps = props => ({
  token: props.token,
});

export default connect(mapStateToProps)(AddWatchModal);

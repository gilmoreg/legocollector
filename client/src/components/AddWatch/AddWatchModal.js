/* eslint-disable jsx-a11y/no-static-element-interactions */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactModal from 'react-modal';
import { connect } from 'react-redux';
import debounce from 'lodash.debounce';
import { API_URL } from '../../config';
import SearchResult from './SearchResult';
import { addWatch } from '../../state/actions';
import './AddWatchModal.css';

export class AddWatchModal extends Component {
  constructor(props) {
    super(props);
    this.submitForm = this.submitForm.bind(this);
    this.state = {
      searchTerm: '',
      searchResult: {},
      error: '',
    };
    this.search = debounce(query => this.queryAPI(query), 250);
    this.onInputChange = this.onInputChange.bind(this);
    this.queryAPI = this.queryAPI.bind(this);
    this.addWatch = this.addWatch.bind(this);
    this.displayError = this.displayError.bind(this);
  }

  onInputChange(event) {
    event.persist();
    if (event.target && event.target.value) {
      const query = event.target.value.trim();
      this.setState({ searchTerm: query });
      if (query) this.search(query);
    }
  }

  queryAPI(query) {
    fetch(`${API_URL}/legoset/search/${query}?token=${this.props.token}`)
      .then(res => res.json())
      .then((res) => {
        if (res && res.result) this.setState({ searchResult: res.result });
        if (res && res.error) this.displayError(res.error);
      })
      .catch(err => this.displayError(err));
  }

  submitForm(event) {
    event.preventDefault();
    this.search();
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
        .then(res => res.result)
        .then((watch) => {
          if (watch && watch.id) {
            this.props.dispatch(addWatch(watch));
            this.props.close();
          }
        })
        .catch(err => this.displayError(err));
    }
  }

  displayError(error) {
    this.setState({ error });
    setTimeout(() => {
      this.setState({ error: '' });
    }, 5000);
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
          <h3>Lego ID:</h3>
          <input
            type="text"
            onChange={this.onInputChange}
          />
          { this.state.error ? <small>{this.state.error}</small> : ''}
        </form>
        {this.state.searchResult.id ?
          <SearchResult
            legoset={this.state.searchResult}
            onClick={this.addWatch}
          />
          : ''}
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

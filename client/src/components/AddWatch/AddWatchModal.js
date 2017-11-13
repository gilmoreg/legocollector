/* eslint-disable jsx-a11y/no-static-element-interactions */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Modal from 'react-modal';
import { connect } from 'react-redux';
import debounce from 'lodash.debounce';
import { API_URL } from '../../config';
import Examples from './Examples';
import SearchResult from './SearchResult';
import { StyledHeader, StyledInput, StyledSmall } from './AddWatchModalStyled';
import Loader from '../Misc/Loader';
import { addWatch, closeModal } from '../../state/actions';
import { digitTest, digitLengthTest } from '../../regexes';
import './AddWatchModal.css';

export class AddWatchModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchTerm: '',
      searchResult: {},
      error: '',
      adding: false,
      searching: false,
      windowHeight: 0,
    };
    this.search = debounce(() => this.queryAPI(), 250);
    this.setSearchTerm = this.setSearchTerm.bind(this);
    this.onInputChange = this.onInputChange.bind(this);
    this.submitForm = this.submitForm.bind(this);
    this.queryAPI = this.queryAPI.bind(this);
    this.addWatch = this.addWatch.bind(this);
    this.displayError = this.displayError.bind(this);
    this.closeModal = this.closeModal.bind(this);
    this.input = { value: '' };
  }

  setSearchTerm(event) {
    try {
      const id = event.target.dataset.id;
      if (id) this.setState({ searchTerm: id });
    } catch (e) {}
  }

  onInputChange(event) {
    event.persist();
    if (event.target && event.target.value) {
      const id = event.target.value.trim();
      if (id && id.match(digitTest)) {
        this.setState({ searchTerm: id });
        this.search();
      }
    }
  }

  submitForm(event) {
    event.preventDefault();
    return this.search();
  }

  queryAPI() {
    this.setState({ searching: true });
    const query = this.state.searchTerm;
    if (!query || !query.match(digitLengthTest)) {
      this.displayError('Set ID must be a 5 to 7 digit number!');
      return Promise.reject();
    }
    return fetch(`${API_URL}/legoset/search/${query}?token=${this.props.token}`)
      .then(res => res.json())
      .then((res) => {
        this.setState({ searching: false });
        if (res.result) this.setState({ searchResult: res.result });
        if (res.error) this.displayError(res.error);
      })
      .catch(err => this.displayError(err));
  }

  addWatch() {
    if (this.state.searchResult.id) {
      // Enable loading spinner
      this.setState({ adding: true });
      return fetch(`${API_URL}/watches/add`, {
        method: 'POST',
        body: JSON.stringify({
          id: this.state.searchResult.id,
          token: this.props.token,
        }),
      })
        .then(res => res.json())
        .then((res) => {
          // Disable loading spinners
          this.setState({ adding: false, searching: false });
          if (res.result) {
            this.props.dispatch(addWatch(res.result));
            this.closeModal();
          }
          if (res.error) {
            this.displayError(res.error);
          }
        })
        .catch(err => this.displayError(err));
    }
  }

  displayError(err) {
    // Disable loading spinners
    this.setState({ adding: false, searching: false });
    let error;
    if (typeof err === 'object') {
      // If we didn't get any response, the API is probably down
      if (!err || Object.keys(err).length === 0) error = 'Error communicating with the server. Please try again later.';
      else error = JSON.stringify(err);
    } else error = err;
    this.setState({ error });
    // Clear error after 5 seconds
    setTimeout(() => {
      this.setState({ error: '' });
    }, 5000);
  }

  closeModal() {
    this.props.dispatch(closeModal());
  }

  render() {
   return (
    <Modal
      isOpen={this.props.open}
      contentLabel="Add New Watch"
      overlayClassName="Overlay"
      className="AddWatchModal"
      shouldCloseOnOverlayClick
      onRequestClose={() => this.closeModal()}
      role="dialog"
      parentSelector={() => document.querySelector('.container')}
    >
      <div className="AddWatchModalContent">
        <form onSubmit={this.submitForm}>
          <StyledHeader>Lego ID:</StyledHeader>
          <Examples click={this.setSearchTerm} />
          <StyledInput
            type="text"
            placeholder={75105}
            onChange={this.onInputChange}
            value={this.state.searchTerm}
          />
          {this.state.error ? <StyledSmall>{this.state.error}</StyledSmall> : ''}
        </form>
        <Loader
          loading={this.state.searching}
          component={this.state.searchResult.id ?
            <SearchResult
              legoset={this.state.searchResult}
              onClick={this.addWatch}
              adding={this.state.adding}
            />
          : <span />}
        />
      </div>
    </Modal>
  );
 }
}

AddWatchModal.defaultProps = {
  open: false,
  dispatch: () => {},
};

AddWatchModal.propTypes = {
  open: PropTypes.bool,
  dispatch: PropTypes.func,
};

const mapStateToProps = props => ({
  open: props.modalOpen,
  token: props.token,
});

export default connect(mapStateToProps)(AddWatchModal);

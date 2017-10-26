import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import debounce from 'lodash.debounce';
import { API_URL } from '../../config';
import SearchResult from './SearchResult';
import { addWatch } from '../../state/actions';

// Only digits, and between 5 and 7 of them
const digitTest = RegExp(/^\d{5,7}$/);

export class AddWatchModalContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchTerm: '',
      searchResult: {},
      error: '',
    };
    this.search = debounce(() => this.queryAPI(), 250);
    this.onInputChange = this.onInputChange.bind(this);
    this.submitForm = this.submitForm.bind(this);
    this.queryAPI = this.queryAPI.bind(this);
    this.addWatch = this.addWatch.bind(this);
    this.displayError = this.displayError.bind(this);
  }

  onInputChange(event) {
    event.persist();
    if (event.target && event.target.value) {
      const query = event.target.value.trim();
      this.setState({ searchTerm: query });
      if (query) this.search();
    }
  }

  submitForm(event) {
    event.preventDefault();
    try {
      const query = event.target.querySelector('input').value;
      this.setState({ searchTerm: query });
      this.search();
    } catch (e) {
      // This is likely to be a ValueError if the querySelector fails
      console.error('submitForm', e);
    }
  }

  queryAPI() {
    const query = this.state.searchTerm;
    if (!query || !query.match(digitTest)) {
      this.displayError('Set ID must be a 5 to 7 digit number!');
      return;
    }
    fetch(`${API_URL}/legoset/search/${query}?token=${this.props.token}`)
      .then(res => res.json())
      .then((res) => {
        if (res && res.result) this.setState({ searchResult: res.result });
        if (res && res.error) this.displayError(res.error);
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
    setTimeout(() => {
      this.setState({ error: '' });
    }, 5000);
  }

  render() {
    return (
      <div className="AddWatchModalContent">
        <form onSubmit={this.submitForm}>
          <h3>Lego ID:</h3>
          <input
            type="text"
            onChange={this.onInputChange}
            placeholder={75105}
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
    );
  }
}

AddWatchModalContent.defaultProps = {
  token: '',
  close: () => {},
  dispatch: () => {},
};

AddWatchModalContent.propTypes = {
  token: PropTypes.string,
  close: PropTypes.func,
  dispatch: PropTypes.func,
};

const mapStateToProps = props => ({
  token: props.token,
});

export default connect(mapStateToProps)(AddWatchModalContent);

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import debounce from 'lodash.debounce';
import { setThreshold } from '../../../state/actions';

import './WatchBody.css';

export class WatchBody extends Component {
  constructor(props) {
    super(props);
    this.state = {
      notifyLevel: 50,
    };
    this.updateSlider = this.updateSlider.bind(this);
    this.updateNotify = this.updateNotify.bind(this);
    this.updateNotify = debounce(this.updateNotify, 1000);
  }

  updateNotify() {
    this.props.dispatch(setThreshold({
      watch: this.props.watch,
      level: this.state.notifyLevel,
    }));
  }

  updateSlider(e) {
    this.setState({ notifyLevel: e.target.value });
    this.updateNotify();
  }

  render() {
    return (
      <div className="WatchBody">
        <div className="graph">
          Fake graph {this.props.watch.title}
        </div>
        <div className="notifications">
          <div className="label">
            Notify me at
          </div>
          <input
            type="range"
            min="1"
            max="100"
            value={this.state.notifyLevel}
            className="slider"
            id="notificatio n-threshold"
            onChange={this.updateSlider}
          />
          <div className="value">
            {this.state.notifyLevel} left
          </div>
        </div>
      </div>
    );
  }
}

WatchBody.propTypes = {
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    currentStock: PropTypes.number.isRequired,
  }).isRequired,
  dispatch: PropTypes.func.isRequired,
};

export default connect()(WatchBody);

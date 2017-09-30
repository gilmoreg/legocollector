import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import CollapsedWatch from './CollapsedWatch/CollapsedWatch';

import './Watch.css';

export class Watch extends Component {
  constructor(props) {
    super(props);
    this.state = {
      collapsed: true,
    }
  }

  render() {
    return (
      <div className="Watch">
        <CollapsedWatch watch={this.props.watch} />
      </div>
    );
  }
}

Watch.propTypes = {
  dispatch: PropTypes.func.isRequired,
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    currentStock: PropTypes.number.isRequired,
  }).isRequired,
}

export default connect()(Watch);

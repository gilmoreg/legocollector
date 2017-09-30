import React from 'react';
import PropTypes from 'prop-types';

import './WatchBody.css';

const WatchBody = props => (
  <div className="WatchBody">
    Hi
  </div>
);

WatchBody.propTypes = {
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    currentStock: PropTypes.number.isRequired,
  }).isRequired,
  click: PropTypes.func.isRequired,
};

export default WatchBody;

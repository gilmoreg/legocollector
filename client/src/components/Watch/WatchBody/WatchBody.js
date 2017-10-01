import React from 'react';
import PropTypes from 'prop-types';

import './WatchBody.css';

const WatchBody = props => (
  <div className="WatchBody">
    <div className="graph">
      Fake graph
    </div>
    <div className="notifications">
      <input
        type="range"
        min="1"
        max="100"
        value="50"
        class="slider"
        id="notification-threshold"
      />
    </div>
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

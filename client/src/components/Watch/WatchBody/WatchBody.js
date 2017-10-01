import React from 'react';
import PropTypes from 'prop-types';

import './WatchBody.css';

const WatchBody = props => (
  <div className="WatchBody">
    <div className="graph">
      Fake graph {props.watch.title}
    </div>
    <div className="notifications">
      <div className="label">
        Notifications
      </div>
      <input
        type="range"
        min="1"
        max="100"
        value="50"
        className="slider"
        id="notification-threshold"
      />
      <div className="value">
        {props.watch.currentStock}
      </div>
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

import React from 'react';
import PropTypes from 'prop-types';
import Chart from './Chart';

import './WatchBody.css';

const WatchBody = props => (
  <div className="WatchBody">
    <Chart stock_levels={props.stock_levels} />
    <button className="delete" onClick={props.deleteWatchClick}>
      <i className="fa fa-times" aria-hidden="true" />
    </button>
  </div>
);

WatchBody.propTypes = {
  stock_levels: PropTypes.arrayOf(PropTypes.shape({
    datetime: PropTypes.string,
    id: PropTypes.number,
    stock_level: PropTypes.number,
  })).isRequired,
  deleteWatchClick: PropTypes.func.isRequired,
};

export default WatchBody;

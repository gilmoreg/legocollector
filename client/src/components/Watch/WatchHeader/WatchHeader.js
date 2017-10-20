/* eslint-disable camelcase */
import React from 'react';
import PropTypes from 'prop-types';

import './WatchHeader.css';

const getCurrentStock = (stock_levels) => {
  const currentLevel = stock_levels[stock_levels.length - 1];
  if (currentLevel) {
    const amount = currentLevel.stock_level;
    if (amount > 999) return '999+';
    return `${amount}`;
  }
  return '-';
};

const WatchHeader = props => (
  <div className="WatchHeader">
    <div className="thumbnail">
      <a href={props.watch.url} target="_blank" rel="noopener noreferrer" title={props.watch.title}>
        <img src={props.watch.image} alt={props.watch.title} />
      </a>
    </div>
    <div className="title">
      <a href={props.watch.url} target="_blank" rel="noopener noreferrer" title={props.watch.title}>
        {props.watch.title}
      </a>
    </div>
    <div className="stock">
      {getCurrentStock(props.watch.stock_levels)}
    </div>
    <button className="delete" onClick={props.deleteClick}>
      <i className="fa fa-times" aria-hidden="true" />
    </button>
  </div>
);

WatchHeader.propTypes = {
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    stock_levels: PropTypes.array.isRequired,
  }).isRequired,
  deleteClick: PropTypes.func.isRequired,
};

export default WatchHeader;

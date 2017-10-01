import React from 'react';
import PropTypes from 'prop-types';

import './WatchHeader.css';

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
      { props.watch.currentStock > 999 ?
        '999+'
        :
        props.watch.currentStock
      }
    </div>
  </div>
);

WatchHeader.propTypes = {
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    currentStock: PropTypes.number.isRequired,
  }).isRequired,
};

export default WatchHeader;

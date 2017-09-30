import React from 'react';
import PropTypes from 'prop-types';

import './CollapsedWatch.css';

const CollapsedWatch = props => (
  <div className="CollapsedWatch">
    <div className="thumbnail">
      <a href={props.watch.url} target='_blank' rel='noopener noreferrer' title={props.watch.title}>
        <img src={props.watch.image} alt={props.watch.title} />
      </a>
    </div>
    <div className="title">
      <a href={props.watch.url} target='_blank' rel='noopener noreferrer' title={props.watch.title}>
        {props.watch.title}
      </a>
    </div>
    <div className="stock">
      {props.watch.currentStock}
    </div>
  </div>
);

CollapsedWatch.propTypes = {
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    currentStock: PropTypes.number.isRequired,
  }).isRequired,
};

export default CollapsedWatch;

import React from 'react';
import PropTypes from 'prop-types';

import './WatchFooter.css';

const UpArrow = () => (<i className="fa fa-angle-double-up" aria-hidden="true" />);
const DownArrow = () => (<i className="fa fa-angle-double-down" aria-hidden="true" />);

const WatchFooter = props => (
  <div className="WatchFooter">
    <button onClick={props.click}>
      { props.collapsed ? <DownArrow /> : <UpArrow /> }
    </button>
  </div>
);

WatchFooter.propTypes = {
  click: PropTypes.func.isRequired,
  collapsed: PropTypes.bool.isRequired,
};

export default WatchFooter;

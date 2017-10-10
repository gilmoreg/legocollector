import React from 'react';
import PropTypes from 'prop-types';

import './AddWatchButton.css';

const AddWatchButton = props => (
  <button className="AddWatchButton" onClick={props.openModal}>
    <span>+</span>
  </button>
);

AddWatchButton.propTypes = {
  openModal: PropTypes.func.isRequired,
};

export default AddWatchButton;

import React from 'react';
import PropTypes from 'prop-types';
import './Loader.css';

const Loader = ({ loading, component }) => (
  <div className="loaderContainer">
    {loading ? <div className="loading" /> : component}
  </div>
);

Loader.propTypes = {
  loading: PropTypes.bool,
  component: PropTypes.element.isRequired,
};

Loader.defaultProps = {
  loading: false,
};

export default Loader;

import React from 'react';
import PropTypes from 'prop-types';
import './Loader.css';

const Loader = ({ loading, component, style }) => (
  <div className={loading ? 'loaderContainer' : ''}>
    {loading ? <div className="loader" /> : component}
  </div>
);

Loader.propTypes = {
  loading: PropTypes.bool,
  component: PropTypes.element,
  style: PropTypes.object,
};

Loader.defaultProps = {
  loading: false,
  component: <span />,
  style: {},
};

export default Loader;

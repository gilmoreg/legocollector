import React from 'react';
import PropTypes from 'prop-types';

const SearchResult = ({ legoset, onClick }) => (
  <div className="SearchResult">
    <a href={legoset.url} rel="noopener noreferrer" target="_blank">
      <img src={legoset.image} alt={legoset.title} />
    </a>
    <h3>
      <a href={legoset.url} rel="noopener noreferrer" target="_blank">
        {legoset.title}
      </a>
    </h3>
    <button onClick={onClick}>Add</button>
  </div>
);

SearchResult.propTypes = {
  legoset: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    image: PropTypes.string,
    url: PropTypes.string,
  }).isRequired,
  onClick: PropTypes.func.isRequired,
};

export default SearchResult;

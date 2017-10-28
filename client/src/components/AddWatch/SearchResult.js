import React from 'react';
import PropTypes from 'prop-types';
import { trimTitle } from '../../regexes';
import './SearchResult.css';

const SearchResult = ({ legoset, onClick }) => (
  <div className="SearchResult">
    <a href={legoset.url} rel="noopener noreferrer" target="_blank">
      <img src={legoset.image} alt={legoset.title} />
    </a>
    <p className="link">
      <a href={legoset.url} rel="noopener noreferrer" target="_blank">
        {trimTitle(legoset.title)}
      </a>
    </p>
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

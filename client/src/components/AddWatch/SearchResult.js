import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import Loader from '../Misc/Loader';
import { trimTitle } from '../../regexes';

const StyledP = styled.p`
  font-size: 24px;
  margin: 0 0.5rem 0 0.5rem;
`;

const StyledImg = styled.img`
  height: 150px;
`;

const SearchResult = ({ legoset, onClick, adding }) => (
  <div className="SearchResult">
    <a href={legoset.url} rel="noopener noreferrer" target="_blank">
      <StyledImg src={legoset.image} alt={legoset.title} />
    </a>
    <StyledP>
      <a href={legoset.url} rel="noopener noreferrer" target="_blank">
        {trimTitle(legoset.title)}
      </a>
    </StyledP>
    <Loader loading={adding} component={<button onClick={onClick}>Add</button>} />
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
  adding: PropTypes.bool.isRequired,
};

export default SearchResult;

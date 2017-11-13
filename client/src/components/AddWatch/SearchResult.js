import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import Loader from '../Misc/Loader';
import { trimTitle } from '../../regexes';

const StyledP = styled.p`
  font-size: 24px;
  margin: 0 0.5rem 0 0.5rem;
  line-height 1.35;
`;

const StyledImg = styled.img`
  height: 150px;
`;

const StyledButton = styled.button`
  background-color: rgba(255,255,255,0.8);
  border: none;
  border-radius: 5px;
  padding: 0.5rem;
  margin: 0.75rem;
  font-size: 24px;
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
    <Loader loading={adding} component={<StyledButton onClick={onClick}>Add</StyledButton>} />
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

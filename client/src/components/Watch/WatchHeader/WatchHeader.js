/* eslint-disable camelcase */
import React from 'react';
import PropTypes from 'prop-types';
import {
  StyledWatchHeader,
  StyledThumbnail,
  StyledImg,
  StyledTitle,
  StyledStock,
  StyledStockP
} from './WatchHeaderStyled';

const getCurrentStock = (stock_levels) => {
  const currentLevel = stock_levels[stock_levels.length - 1];
  if (currentLevel) {
    const amount = currentLevel.stock_level;
    if (amount > 999) return '999+';
    return `${amount}`;
  }
  return '-';
};

const WatchHeader = props => (
  <StyledWatchHeader>
    <StyledThumbnail>
      <a href={props.watch.url} target="_blank" rel="noopener noreferrer" title={props.watch.title}>
        <StyledImg src={props.watch.image} alt={props.watch.title} />
      </a>
    </StyledThumbnail>
    <StyledTitle>
      <a href={props.watch.url} target="_blank" rel="noopener noreferrer" title={props.watch.title}>
        {props.watch.title}
      </a>
    </StyledTitle>
    <StyledStock>
      {getCurrentStock(props.watch.stock_levels)}
      <StyledStockP>in stock</StyledStockP>
    </StyledStock>
  </StyledWatchHeader>
);

WatchHeader.propTypes = {
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    stock_levels: PropTypes.array.isRequired,
  }).isRequired,
};

export default WatchHeader;

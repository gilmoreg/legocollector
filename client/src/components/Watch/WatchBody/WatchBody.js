import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import Chart from './Chart';

const StyledDiv = styled.div`
  background-color: rgba(255,246,229,0.7);
  max-width: 760px;
  margin: 0 auto;
  position: relative;
  padding-top: 1rem;
  z-index: -2;
`;

const StyledButton = styled.button`
  position: absolute;
  top: 1px;
  right: 1px;
  font-size: 30px;
  background-color: rgba(255,246,229,0);
  color: #3E454C;
  border: none;
`;

const WatchBody = props => (
  <StyledDiv>
    <Chart stock_levels={props.stock_levels} />
    <StyledButton className="delete" onClick={props.deleteWatchClick}>
      <i className="fa fa-times" aria-hidden="true" />
    </StyledButton>
  </StyledDiv>
);

WatchBody.propTypes = {
  stock_levels: PropTypes.arrayOf(PropTypes.shape({
    datetime: PropTypes.string,
    id: PropTypes.number,
    stock_level: PropTypes.number,
  })).isRequired,
  deleteWatchClick: PropTypes.func.isRequired,
};

export default WatchBody;

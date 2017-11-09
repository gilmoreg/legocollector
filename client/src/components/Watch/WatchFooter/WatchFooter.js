import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledButton = styled.button`
  display: block;
  background-color: rgba(255,246,229,0.7);
  border: none;
  border-radius: 0px 0px 5px 5px;
  max-width: 760px;
  width: 100%;
  margin: 0 auto;
  z-index: -2;
`;

const UpArrow = () => (<i className="fa fa-angle-double-up" aria-hidden="true" />);
const DownArrow = () => (<i className="fa fa-angle-double-down" aria-hidden="true" />);

const WatchFooter = props => (
  <div className="WatchFooter">
    <StyledButton onClick={props.click}>
      { props.collapsed ? <DownArrow /> : <UpArrow /> }
    </StyledButton>
  </div>
);

WatchFooter.propTypes = {
  click: PropTypes.func.isRequired,
  collapsed: PropTypes.bool.isRequired,
};

export default WatchFooter;

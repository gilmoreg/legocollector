import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledButton = styled.button`
  border: 10px solid #FF7F66;
  border-radius: 50%;
  background-color: #FF7F66;
  width: 50px;
  height: 50px;
  position: fixed;
  bottom: 50px;
  right: 25px;
  z-index: 0;
`;

const StyledSpan = styled.span`
  color: white;
  font-size: 40px;
  position: relative;
  top: -12px;
  left: -3px;
  content: "+";
`;

const AddWatchButton = props => (
  <StyledButton onClick={props.openModal}>
    <StyledSpan>+</StyledSpan>
  </StyledButton>
);

AddWatchButton.propTypes = {
  openModal: PropTypes.func.isRequired,
};

export default AddWatchButton;

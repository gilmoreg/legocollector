import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledButton = styled.button`
  border: none;
  background-color: rgba(255,255,255,0);
  font-size: 14px;
  text-align: left;
  &:hover {
    color: #FF7F66;
  }
`;

const StyledUL = styled.ul`
  font-size: 12px;
  margin-top: 0.25rem;
  margin-left: 0;
  padding-left: 1rem;
  text-align: left;
  list-style: none;

  @media (min-width: 768px) {
    text-align: center;
  }
`;

const StyledH4 = styled.h4`
  font-size: 14px;
  margin-bottom: 0.25rem;
`;

const Examples = (props) => (
  <div className="Examples">
    <StyledH4>Examples (click to test out):</StyledH4>
    <StyledUL>
      <li key="75105">
        <StyledButton data-id={75105} onClick={props.click}>75105 - Star Wars Millenium Falcon</StyledButton>
      </li>
      <li key="21029">
        <StyledButton data-id={21029} onClick={props.click}>21029 - Architecture Buckingham Palace</StyledButton>
      </li>
      <li key="10232">
        <StyledButton data-id={10232} onClick={props.click}>10232 - Modular Buildings Palace Cinema</StyledButton>
      </li>
      <li key="10217">
        <StyledButton data-id={10217} onClick={props.click}>10217 - Harry Potter Diagon Alley</StyledButton>
      </li>
    </StyledUL>
  </div>
);

Examples.propTypes = {
  click: PropTypes.func.isRequired,
}

export default Examples;

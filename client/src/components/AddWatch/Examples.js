import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import './Examples.css';

const StyledButton = styled.button`
  text-align: left;
  &:hover {
    color: #FF7F66;
  }
`;

const Examples = (props) => (
  <div className="Examples">
    <h4>Examples (click to test out):</h4>
    <ul>
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
    </ul>
  </div>
);

Examples.propTypes = {
  click: PropTypes.func.isRequired,
}

export default Examples;

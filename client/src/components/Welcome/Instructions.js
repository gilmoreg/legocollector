import React from 'react';
import styled from 'styled-components';

const StyledInstructions = styled.div`
  position: fixed;
  bottom: 110px;
  right: 25px;
  border-radius: 5px;
  background-color: rgba(255,246,229,0.7);
  padding: 1rem;
  z-index: -1;
`;

const StyledPlus = styled.div`
  display: inline-block;
  border: 0.5rem solid #FF7F66;
  border-radius: 100%;
  background-color: #FF7F66;
  color: white;
  width: 2rem;
  height: 2rem;
  font-size: 14px;
`;

const Instructions = () => (
  <StyledInstructions>
    Click on the <StyledPlus>+</StyledPlus> to start watching sets!
  </StyledInstructions>
);

export default Instructions;

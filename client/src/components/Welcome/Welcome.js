import React from 'react';
import styled from 'styled-components';
import Login from '../Auth/Login';

const StyledWelcome = styled.div`
  background-color: rgba(255,246,229,0.7);
  border-radius: 5px;
  margin: 1rem;
  padding: 1rem;
  margin-bottom: 4rem;

  @media (min-width: 768px) {
    font-size: 28px;
  }
`;

const StyledP = styled.p`
  text-align: left;

  @media (min-width: 768px) {
    text-align: center;
  }
`;

const StyledImages = styled.div`
  text-align: center;
`;

const StyledImg = styled.img`
  margin: 0.5rem;
`;

const Welcome = () => (
  <StyledWelcome>
    <h2>Welcome to Lego Collector!</h2>
    <StyledP>
      If you collect Lego sets for profit, you always want to know when a set is about to run
      out of stock. Lego Collector keeps you up to date by tracking Amazon&#39;s stock levels
      for Lego sets you specify.
    </StyledP>
    <StyledImages>
    <StyledImg
        src="https://res.cloudinary.com/dk85nueap/image/upload/c_scale,h_240,w_256/v1509734315/gilmoreg.github.io-legocollector-_iPhone_6_1_tvqhpj.png"
        alt="example list view"
      />
      <StyledImg
        src="https://res.cloudinary.com/dk85nueap/image/upload/c_scale,w_256/v1509733347/gilmoreg.github.io-legocollector-_iPhone_6_zed1iv.png"
        alt="example stock levels"
      />
    </StyledImages>
    <StyledP>
      Check the stock levels of all the sets you have your eye on in one convenient place!
    </StyledP>
    <div><Login /></div>
  </StyledWelcome>
);

export default Welcome;

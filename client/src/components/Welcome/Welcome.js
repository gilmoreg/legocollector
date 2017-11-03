import React from 'react';
import Login from '../Auth/Login';
import './Welcome.css';

const Welcome = () => (
  <div className="Welcome">
    <h2>Welcome to Lego Collector!</h2>
    <p>
      If you collect Lego sets for profit, you always want to know when a set is about to run
      out of stock. Lego Collector keeps you up to date by tracking Amazon&#39;s stock levels
      for Lego sets you specify.
    </p>
    <div className="images">
    <img
        src="http://res.cloudinary.com/dk85nueap/image/upload/c_scale,h_240,w_256/v1509734315/gilmoreg.github.io-legocollector-_iPhone_6_1_tvqhpj.png"
        alt="example list view"
      />
      <img
        src="http://res.cloudinary.com/dk85nueap/image/upload/c_scale,w_256/v1509733347/gilmoreg.github.io-legocollector-_iPhone_6_zed1iv.png"
        alt="example stock levels"
      />
    </div>
    <p>
      Check the stock levels of all the sets you have your eye on in one convenient place!
    </p>
    <div><Login /></div>
  </div>
);

export default Welcome;

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
    <p>
      Check the stock levels of all the sets you have your eye on in one convenient place!
    </p>
    <div><Login /></div>
  </div>
);

export default Welcome;

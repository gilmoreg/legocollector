import React from 'react';
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
    <p>
      Soon it will be able to notify you via email when a certain
      stock falls below a threshold you define so you can snap up one of the last sets before
      it&#39;s too late!
    </p>
  </div>
);

export default Welcome;

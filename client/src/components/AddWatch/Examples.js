import React from 'react';
import PropTypes from 'prop-types';
import './Examples.css';

const Examples = (props) => (
  <div className="Examples">
    <h4>Examples (click to test out):</h4>
    <ul>
      <li key="75105">
        <button data-id={75105} onClick={props.click}>75105 - Star Wars Millenium Falcon</button>
      </li>
      <li key="21029">
        <button data-id={21029} onClick={props.click}>21029 - Architecture Buckingham Palace</button>
      </li>
      <li key="10232">
        <button data-id={10232} onClick={props.click}>10232 - Modular Buildings Palace Cinema</button>
      </li>
      <li key="10217">
        <button data-id={10217} onClick={props.click}>10217 - Harry Potter Diagon Alley</button>
      </li>
    </ul>
  </div>
);

Examples.propTypes = {
  click: PropTypes.func.isRequired,
}

export default Examples;

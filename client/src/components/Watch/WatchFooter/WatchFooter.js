import React from 'react';
import PropTypes from 'prop-types';

import './WatchFooter.css';

const WatchFooter = props => (
  <div className="WatchFooter">
    <button onClick={props.click}>
			{ props.collapsed ?
				<i class="fa fa-angle-double-down" aria-hidden="true"></i>
				:
				<i class="fa fa-angle-double-up" aria-hidden="true"></i>
			}
		</button>
  </div>
);

WatchFooter.propTypes = {
	click: PropTypes.func.isRequired,
	collapsed: PropTypes.bool.isRequired,
}

export default WatchFooter;

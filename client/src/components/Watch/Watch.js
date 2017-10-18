import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import WatchHeader from './WatchHeader/WatchHeader';
import WatchBody from './WatchBody/WatchBody';
import WatchFooter from './WatchFooter/WatchFooter';

import './Watch.css';

export class Watch extends Component {
  constructor(props) {
    super(props);
    this.state = {
      collapsed: true,
    };
  }

  render() {
    return (
      <div className="Watch">
        <WatchHeader watch={this.props.watch} />
        { this.state.collapsed ?
          <div />
          :
          <WatchBody
            watch={this.props.watch}
          />
        }
        <WatchFooter
          click={() => this.setState({
            collapsed: !this.state.collapsed,
          })}
          collapsed={this.state.collapsed}
        />
      </div>
    );
  }
}

Watch.propTypes = {
  // dispatch: PropTypes.func.isRequired,
  watch: PropTypes.shape({
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    stock_levels: PropTypes.array.isRequired,
  }).isRequired,
};

export default connect()(Watch);

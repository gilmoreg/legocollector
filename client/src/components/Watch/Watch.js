import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import WatchHeader from './WatchHeader/WatchHeader';
import WatchBody from './WatchBody/WatchBody';
import WatchFooter from './WatchFooter/WatchFooter';
import { deleteWatch } from '../../state/actions';

import './Watch.css';

export class Watch extends Component {
  constructor(props) {
    super(props);
    this.state = {
      collapsed: true,
    };
    this.deleteWatchClick = this.deleteWatchClick.bind(this);
  }

  deleteWatchClick() {
    this.props.dispatch(deleteWatch(this.props.token, this.props.watch.id));
  }

  render() {
    return (
      <div className="Watch">
        <WatchHeader
          watch={this.props.watch}
          deleteClick={this.deleteWatchClick}
        />
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

Watch.defaultProps = {
  token: '',
};

Watch.propTypes = {
  dispatch: PropTypes.func.isRequired,
  watch: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    image: PropTypes.string,
    url: PropTypes.string,
    stock_levels: PropTypes.array,
  }).isRequired,
  token: PropTypes.string,
};

const mapStateToProps = state => ({
  token: state.token,
});

export default connect(mapStateToProps)(Watch);

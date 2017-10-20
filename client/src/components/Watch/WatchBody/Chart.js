import React from 'react';
import PropTypes from 'prop-types';
// https://github.com/jerairrest/react-chartjs-2/blob/master/example/src/components/line.js
import { Line } from 'react-chartjs-2';
import moment from 'moment';
import './Chart.css';

const Chart = (props) => {
  const data = {
    labels: props.stock_levels.map(level =>
      moment(new Date(level.datetime)).format('MM-DD')),
    datasets: [
      {
        label: false,
        fill: false,
        lineTension: 0.1,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBorderColor: 'rgba(75,192,192,1)',
        pointBackgroundColor: '#fff',
        pointBorderWidth: 1,
        pointHoverRadius: 5,
        pointHoverBackgroundColor: 'rgba(75,192,192,1)',
        pointHoverBorderColor: 'rgba(220,220,220,1)',
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: props.stock_levels.map(level => level.stock_level),
      },
    ],
  };
  const options = {
    legend: {
      display: false,
    },
  };

  return (
    <div className="Chart">
      <Line data={data} options={options} />
    </div>
  );
};

Chart.propTypes = {
  stock_levels: PropTypes.arrayOf(PropTypes.shape({
    datetime: PropTypes.string,
    id: PropTypes.number,
    stock_level: PropTypes.number,
  })).isRequired,
};

export default Chart;

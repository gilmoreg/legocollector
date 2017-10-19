import React from 'react';
import PropTypes from 'prop-types';
import { LineChart } from 'react-chartjs-2';

const Chart = (props) => {
  const createPoints = data =>
    data.map((point, index) => ({
      x: index,
      y: point.stock_level,
    }));

  const data = [
    {
      color: 'steelblue',
      points: createPoints(props.stock_levels),
    },
  ];

  return (
    <LineChart
      width={600}
      height={200}
      data={data}
      hideXLabel
      hideYLabel
      hideXAxis
      hideYAxis
    />
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

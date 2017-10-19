import React from 'react';
import PropTypes from 'prop-types';
import LineChart from 'react-linechart';
// import moment from 'moment';

const Chart = (props) => {
  // const formatDate = date => moment(date).format('YYYY-MM-DD');

  const createPoints = data =>
    data.map((point, index) => ({
      x: index, // formatDate(point.datetime),
      y: point.stock_level,
    }));

  const data = [
    {
      color: 'steelblue',
      points: createPoints(props.stock_levels),
      // isDate: true,
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

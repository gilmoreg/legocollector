import React from 'react';
import { shallow } from 'enzyme';
import Chart from './Chart';

it('renders without crashing', () => {
  const stockLevels = [
    { datetime: 'test', stock_level: 1 },
    { datetime: 'test', stock_level: 1 },
  ];
  const wrapper = shallow(
    <Chart stock_levels={stockLevels} />,
  );
  expect(wrapper).toMatchSnapshot();
});

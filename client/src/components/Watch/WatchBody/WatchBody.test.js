import React from 'react';
import { shallow } from 'enzyme';
import WatchBody from './WatchBody';

it('renders without crashing', () => {
  const stockLevels = [
    { datetime: 'test', stock_level: 1 },
    { datetime: 'test', stock_level: 1 },
  ];
  const wrapper = shallow(
    <WatchBody
      stock_levels={stockLevels}
      deleteWatchClick={() => {}}
    />,
  );
  expect(wrapper).toMatchSnapshot();
});

import React from 'react';
import { shallow } from 'enzyme';
import { WatchBody } from './WatchBody';

it('renders without crashing', () => {
  const watch = {
    title: 'test',
    image: 'test',
    url: 'test',
    stock_levels: [
      { datetime: 'test', stock_level: 1 },
      { datetime: 'test', stock_level: 1 },
    ],
  };
  const wrapper = shallow(
    <WatchBody watch={watch} dispatch={() => {}} click={() => {}} />,
  );
  expect(wrapper).toMatchSnapshot();
});

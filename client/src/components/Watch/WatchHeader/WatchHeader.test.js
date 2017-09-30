import React from 'react';
import { shallow } from 'enzyme';
import WatchHeader from './WatchHeader';

it('renders without crashing', () => {
  const watch = {
    title: 'test',
    image: 'test',
    url: 'test',
    currentStock: 0,
  }
  const wrapper = shallow(
    <WatchHeader watch={watch} />
  );
  expect(wrapper).toMatchSnapshot();
});

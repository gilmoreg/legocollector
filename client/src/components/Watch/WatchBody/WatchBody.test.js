import React from 'react';
import { shallow } from 'enzyme';
import WatchBody from './WatchBody';

it('renders without crashing', () => {
  const watch = {
    title: 'test',
    image: 'test',
    url: 'test',
    currentStock: 0,
  }
  const wrapper = shallow(
    <WatchBody watch={watch} click={()=>{}}/>
  );
  expect(wrapper).toMatchSnapshot();
});

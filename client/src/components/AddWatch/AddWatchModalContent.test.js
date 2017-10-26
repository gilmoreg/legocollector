import React from 'react';
import { shallow } from 'enzyme';
import { AddWatchModalContent } from './AddWatchModalContent';

it('renders without crashing', () => {
  const wrapper = shallow(
    <AddWatchModalContent
      open={false}
      close={() => {}}
    />);
  expect(wrapper).toMatchSnapshot();
});
import React from 'react';
import { shallow } from 'enzyme';
import AddWatchButton from './AddWatchButton';

it('renders without crashing', () => {
  const wrapper = shallow(
    <AddWatchButton openModal={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

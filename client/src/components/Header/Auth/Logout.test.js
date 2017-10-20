import React from 'react';
import { shallow } from 'enzyme';
import { Logout } from './Logout';

it('renders without crashing', () => {
  const wrapper = shallow(
    <Logout dispatch={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

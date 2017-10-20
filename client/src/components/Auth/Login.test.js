import React from 'react';
import { shallow } from 'enzyme';
import { Login } from './Login';

it('renders without crashing', () => {
  const wrapper = shallow(
    <Login dispatch={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

import React from 'react';
import { shallow } from 'enzyme';
import { Logout } from './Logout';

it('renders without crashing', () => {
  const wrapper = shallow(<Logout dispatch={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

it('logs out without crashing', () => {
  window.localStorage = { removeItem: jest.fn() };
  const wrapper = shallow(<Logout dispatch={jest.fn()} />);
  wrapper.instance().logout();
  expect(window.localStorage.removeItem).toHaveBeenCalled();
  expect(wrapper.instance().props.dispatch).toHaveBeenCalled();
  window.localStorage = undefined;
});

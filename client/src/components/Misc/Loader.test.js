import React from 'react';
import { shallow } from 'enzyme';
import Loader from './Loader';

it('renders without crashing', () => {
  const wrapper = shallow(<Loader />);
  expect(wrapper).toMatchSnapshot();
});

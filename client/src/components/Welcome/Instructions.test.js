import React from 'react';
import { shallow } from 'enzyme';
import Instructions from './Instructions';

it('renders without crashing', () => {
  const wrapper = shallow(
    <Instructions />,
  );
  expect(wrapper).toMatchSnapshot();
});

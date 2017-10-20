import React from 'react';
import { shallow } from 'enzyme';
import Welcome from './Welcome';

it('renders without crashing', () => {
  const wrapper = shallow(
    <Welcome />,
  );
  expect(wrapper).toMatchSnapshot();
});

import React from 'react';
import { shallow } from 'enzyme';
import Examples from './Examples';

it('renders without crashing', () => {
  const wrapper = shallow(
    <Examples click={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

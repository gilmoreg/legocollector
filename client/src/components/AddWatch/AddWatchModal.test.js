import React from 'react';
import { shallow } from 'enzyme';
import { AddWatchModal } from './AddWatchModal';

it('renders without crashing', () => {
  const wrapper = shallow(
    <AddWatchModal open close={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

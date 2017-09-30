import React from 'react';
import { shallow } from 'enzyme';
import CollapsedWatch from './CollapsedWatch';

it('renders without crashing', () => {
  const watch = {
    title: 'test',
    image: 'test',
    url: 'test',
    currentStock: 0,
  }
  const wrapper = shallow(
    <CollapsedWatch watch={watch} />
  );
  expect(wrapper).toMatchSnapshot();
});

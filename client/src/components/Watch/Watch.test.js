import React from 'react';
import { shallow } from 'enzyme';
import { Watch } from './Watch';

it('renders without crashing', () => {
  const wrapper = shallow(
    <Watch dispatch={()=>{}}/>
  );
  expect(wrapper).toMatchSnapshot();
});

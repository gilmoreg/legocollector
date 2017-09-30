import React from 'react';
import { shallow } from 'enzyme';
import WatchFooter from './WatchFooter';

it('renders without crashing', () => {
  const wrapper = shallow(
    <WatchFooter click={()=>{}}/>
  );
  expect(wrapper).toMatchSnapshot();
});

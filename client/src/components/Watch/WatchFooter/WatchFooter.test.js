import React from 'react';
import { shallow } from 'enzyme';
import WatchFooter from './WatchFooter';

it('renders collapsed without crashing', () => {
  const wrapper = shallow(
    <WatchFooter click={()=>{}} collapsed={true} />
  );
  expect(wrapper).toMatchSnapshot();
});

it('renders not collapsed without crashing', () => {
  const wrapper = shallow(
    <WatchFooter click={()=>{}} collapsed={false} />
  );
  expect(wrapper).toMatchSnapshot();
});

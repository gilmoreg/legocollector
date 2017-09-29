import React from 'react';
import { shallow, configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { Login } from './Login';

configure({ adapter: new Adapter() });

it('renders without crashing', () => {
  const div = document.createElement('div');
  const wrapper = shallow(
    <Login dispatch={()=>{}}/>);
  expect(wrapper).toMatchSnapshot();
});

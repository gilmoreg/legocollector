import React from 'react';
import { shallow, configure } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { App } from './App';

configure({ adapter: new Adapter() });

it('renders without crashing', () => {
  const div = document.createElement('div');
  window.localStorage = {
    getItem: () => JSON.stringify({
      email: 'test@test.com',
      token: '123',
    }),
  }

  const wrapper = shallow(
    <App dispatch={()=>{}} />
  );
  expect(wrapper).toMatchSnapshot();
  window.localStorage = undefined;
});

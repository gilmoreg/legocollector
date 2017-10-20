import React from 'react';
import { shallow } from 'enzyme';
import { App } from './App';

it('renders without crashing', () => {
  window.localStorage = {
    getItem: () => JSON.stringify({
      email: 'test@test.com',
      token: '123',
    }),
  };

  const wrapper = shallow(
    <App dispatch={() => {}} />,
  );
  expect(wrapper).toMatchSnapshot();
  window.localStorage = undefined;
});

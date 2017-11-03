import React from 'react';
import { shallow } from 'enzyme';
import fetchMock from 'fetch-mock';
import { Login } from './Login';
import * as fakes from '../../../../utils/fakes';

it('renders without crashing', () => {
  const wrapper = shallow(<Login dispatch={() => {}} />);
  expect(wrapper).toMatchSnapshot();
});

it('amazonLogin calls fetchProfile with a token', async (done) => {
  // Mock API call
  fetchMock.catch(500);
  fetchMock.mock(/.login/, fakes.fakeProfileResponse);
  // Mock Amazon object
  window.amazon = { Login: { authorize: (options, callback) =>
    callback({ access_token: 'test' })}};
  
  const wrapper = shallow(<Login dispatch={jest.fn()} />);
  await wrapper.instance().amazonLogin();
  expect(global.localStorage.setItem).toHaveBeenCalled();
  expect(wrapper.instance().props.dispatch).toHaveBeenCalledTimes(2);
  // Cleanup
  window.amazon = undefined;
  fetchMock.restore();
  jest.resetAllMocks();
  localStorage.clear();
  done();
});

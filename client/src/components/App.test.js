import React from 'react';
import { shallow } from 'enzyme';
import { App } from './App';
import * as fakes from '../../utils/fakes';

it('renders without crashing', () => {
  window.localStorage = fakes.fakeLocalStorageProfile;
  const wrapper = shallow(
    <App dispatch={() => {}} />,
  );
  expect(wrapper).toMatchSnapshot();
  window.localStorage = undefined;
});

it('renders without crashing with no profile in localstorage', () => {
  window.localStorage = fakes.fakeLocalStorageNoProfile;
  const wrapper = shallow(
    <App dispatch={() => {}} />,
  );
  expect(wrapper).toMatchSnapshot();
  window.localStorage = undefined;
});

it('renders without crashing logged in with a watch', () => {
  window.localStorage = fakes.fakeLocalStorageProfile;
  const wrapper = shallow(
    <App dispatch={() => {}} watches={[fakes.fakeWatch]} loggedIn />,
  );
  // Snapshot won't work here beacuse of timestamp in watch
  expect(wrapper.instance().props.watches.length).toEqual(1);
  window.localStorage = undefined;
});

it('renders without crashing logged in with no watches', () => {
  window.localStorage = fakes.fakeLocalStorageProfile;
  const wrapper = shallow(
    <App dispatch={() => {}} loggedIn />,
  );
  expect(wrapper).toMatchSnapshot();
  window.localStorage = undefined;
});

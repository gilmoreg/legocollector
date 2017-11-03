import React from 'react';
import { shallow } from 'enzyme';
import fetchMock from 'fetch-mock';
import { App } from './App';
import * as fakes from '../../utils/fakes';

describe('App Component tests', () => {
  beforeAll(() => fetchMock.catch(500));
  afterAll(() => fetchMock.restore());

  it('renders without crashing', () => {
    fetchMock.mock(/.+/, { message: 'success' });
    window.localStorage = fakes.fakeLocalStorageProfile;
    const wrapper = shallow(
      <App dispatch={() => {}} />,
    );
    expect(wrapper).toMatchSnapshot();
    window.localStorage = undefined;
  });
  
  it('renders without crashing with no profile in localstorage', () => {
    fetchMock.mock(/.+/, { message: 'success' });
    window.localStorage = fakes.fakeLocalStorageNoProfile;
    const wrapper = shallow(
      <App dispatch={() => {}} />,
    );
    expect(wrapper).toMatchSnapshot();
    window.localStorage = undefined;
  });
  
  it('renders without crashing logged in with a watch', () => {
    fetchMock.mock(/.+/, { message: 'success' });
    window.localStorage = fakes.fakeLocalStorageProfile;
    const wrapper = shallow(
      <App dispatch={() => {}} watches={[fakes.fakeWatch]} loggedIn />,
    );
    // Snapshot won't work here beacuse of timestamp in watch
    expect(wrapper.instance().props.watches.length).toEqual(1);
    window.localStorage = undefined;
  });
  
  it('renders without crashing logged in with no watches', () => {
    fetchMock.mock(/.+/, { message: 'success' });
    window.localStorage = fakes.fakeLocalStorageProfile;
    const wrapper = shallow(
      <App dispatch={() => {}} loggedIn />,
    );
    expect(wrapper).toMatchSnapshot();
    window.localStorage = undefined;
  });
});


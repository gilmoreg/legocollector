import React from 'react';
import fetchMock from 'fetch-mock';
import { shallow } from 'enzyme';
import { AddWatchModal } from './AddWatchModal';
import * as fakes from '../../../utils/fakes';

jest.useFakeTimers();

describe('AddWatchModal tests', () => {
  beforeEach(() => fetchMock.catch(500));
  afterEach(() => fetchMock.restore());
  
  it('renders without crashing', () => {
    const wrapper = shallow(
      <AddWatchModal open close={() => {}} />);
    expect(wrapper).toMatchSnapshot();
  });
  
  /*
  A few tests seem necessary:
  1. Submitting the form
  2. Typing in the search box
  3. Doing both of these with successes and errors
  it('') 
  */
  
  it('query the API on a valid input', (done) => {
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().queryAPI = jest.fn();
    // Set searchTerm to something that will pass digitTest
    wrapper.instance().setState({ searchTerm: '00000' });
    // Simulate a form submit
    wrapper.find('form').simulate('submit', { preventDefault () {} });
    // Expire timers in debounce
    jest.runAllTimers();
    expect(wrapper.instance().queryAPI).toHaveBeenCalled();
    done();    
  });

  it('queryAPI sets searchResult on good input', async (done) => {
    fetchMock.mock(/.legoset./, fakes.fakeSearchSuccess);
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    // Set searchTerm to something that will pass digitTest
    wrapper.instance().setState({ searchTerm: '00000' });
    await wrapper.instance().queryAPI();
    expect(wrapper.instance().state.searchResult).toEqual(fakes.fakeSearchResult);
    done();
  });
  
  it('queryAPI displays error on invalid input', async (done) => {
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    // Set searchTerm to something that will pass digitTest
    wrapper.instance().setState({ searchTerm: '0' });
    wrapper.instance().displayError = jest.fn();
    try {
      await wrapper.instance().queryAPI();
    } catch (e) {
      expect(wrapper.instance().displayError).toHaveBeenCalled();
      done();
    }
  });

  it('queryAPI displays error when API is down', async (done) => {
    // fetchMock.catch should time out the API call
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState({ searchTerm: '00000' });
    wrapper.instance().displayError = jest.fn();
    await wrapper.instance().queryAPI();
    expect(wrapper.instance().displayError).toHaveBeenCalled();
    done();
  });

  it('queryAPI displays error when error returned from API', async (done) => {
    fetchMock.mock(/.legoset./, fakes.fakeSearchError);
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    // Set searchTerm to something that will pass digitTest
    wrapper.instance().setState({ searchTerm: '00000' });
    wrapper.instance().displayError = jest.fn();
    await wrapper.instance().queryAPI();
    expect(wrapper.instance().displayError).toHaveBeenCalled();
    done();
  });
});

/*
Scratch:
setImmediate(() => {
  jest.runAllTimers();
  console.log(wrapper.update().instance().setState.mock);
  done();
});
// Expire timers in throttle
    // jest.runAllTimers();
    // expect(wrapper.instance().displayError).toHaveBeenCalled();
*/

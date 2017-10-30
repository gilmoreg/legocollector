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
  
  it('setSearchTerm sets searchTerm', () => {
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState = jest.fn();
    const event = {
      target: { dataset: { id: '00000' }}
    }
    wrapper.instance().setSearchTerm(event);
    expect(wrapper.instance().setState).toHaveBeenCalled();
  });

  it('setSearchTerm errors on invalid input', () => {
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState = jest.fn();
    // Empty object for event should throw an error
    wrapper.instance().setSearchTerm({});
    expect(wrapper.instance().setState).not.toHaveBeenCalled();
  });

  it('onInputChange should setState and search on valid input', () => {
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState = jest.fn();
    wrapper.instance().search = jest.fn();
    const event = {
      persist: jest.fn(),
      target: { value: '00000' }
    }
    wrapper.instance().onInputChange(event);
    expect(wrapper.instance().setState).toHaveBeenCalled();
    expect(wrapper.instance().search).toHaveBeenCalled();
  });

  it('onInputChange should not setState or search on invalid input', () => {
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState = jest.fn();
    wrapper.instance().search = jest.fn();
    const event = {
      persist: jest.fn(),
      target: { value: 'abc' } // characters fail digitTest
    }
    wrapper.instance().onInputChange(event);
    expect(wrapper.instance().setState).not.toHaveBeenCalled();
    expect(wrapper.instance().search).not.toHaveBeenCalled();
  });

  
  it('submitting form should query the API on a valid input', (done) => {
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
    fetchMock.mock(/.legoset./, 500);
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

  it('addWatch should close modal if successful', async (done) => {
    fetchMock.mock(/.watches./, fakes.fakeAddWatchSuccess);
    const wrapper = shallow(<AddWatchModal open close={jest.fn()} />);
    wrapper.instance().setState({ searchResult: fakes.fakeSearchResult });
    await wrapper.instance().addWatch();
    expect(wrapper.instance().props.close).toHaveBeenCalled();
    done();
  });

  it('addWatch should displayError if unsuccessful', async (done) => {
    fetchMock.mock(/.watches./, fakes.fakeAddWatchError);
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState({ searchResult: fakes.fakeSearchResult });
    wrapper.instance().displayError = jest.fn();
    await wrapper.instance().addWatch();
    expect(wrapper.instance().displayError).toHaveBeenCalled();
    done();
  });

  it('addWatch should displayError if API call fails', async (done) => {
    fetchMock.mock(/.watches./, 500);
    const wrapper = shallow(<AddWatchModal open close={() => {}} />);
    wrapper.instance().setState({ searchResult: fakes.fakeSearchResult });
    wrapper.instance().displayError = jest.fn();
    await wrapper.instance().addWatch();
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

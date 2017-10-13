import React from 'react';
import { shallow } from 'enzyme';
import SearchResult from './SearchResult';

it('renders without crashing', () => {
  const wrapper = shallow(
    <SearchResult
      legoset={{
        id: 0,
        title: 'Test',
        image: 'test',
        url: 'test',
      }}
      onClick={() => {}}
    />);
  expect(wrapper).toMatchSnapshot();
});

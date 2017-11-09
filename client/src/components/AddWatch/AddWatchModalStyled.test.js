import React from 'react';
import { shallow } from 'enzyme';
import { StyledHeader, StyledInput, StyledSmall } from './AddWatchModalStyled';

describe('Test styled components for AddWatchModal', () => {
  it('StyledHeader renders without crashing', () => {
    const wrapper = shallow(
      <StyledHeader />);
    expect(wrapper).toMatchSnapshot();
  });

  it('StyledInput renders without crashing', () => {
    const wrapper = shallow(
      <StyledInput />);
    expect(wrapper).toMatchSnapshot();
  });

  it('StyledSmall renders without crashing', () => {
    const wrapper = shallow(
      <StyledSmall />);
    expect(wrapper).toMatchSnapshot();
  });
});
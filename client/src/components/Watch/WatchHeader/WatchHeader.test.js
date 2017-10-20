import React from 'react';
import { shallow } from 'enzyme';
import WatchHeader from './WatchHeader';

it('renders without crashing', () => {
  const fakeWatch = {
    title: 'LEGO Ideas NASA Apollo Saturn V 21309 Building Kit',
    image: 'https://images-na.ssl-images-amazon.com/images/I/413yqVUgjcL._SL160_.jpg',
    url: 'https://www.amazon.com/LEGO-Ideas-Apollo-Saturn-Building/dp/B01MUANC80?psc=1&SubscriptionId=AKIAJ57KMBTCZPRJ5I5Q&tag=gilmoreg-20&linkCode=xm2&camp=2025&creative=165953&creativeASIN=B01MUANC80',
    stock_levels: [
      { datetime: 'test', stock_level: 1 },
      { datetime: 'test', stock_level: 1 },
    ],
  };
  const wrapper = shallow(
    <WatchHeader watch={fakeWatch} deleteClick={() => {}} />,
  );
  expect(wrapper).toMatchSnapshot();
});

/* eslint-disable import/prefer-default-export */
export const fakeWatch = {
  id: 0,
  image: 'test',
  url: 'test',
  title: 'test',
  added: Date.now(),
  stock_levels: [
    { datetime: Date.now(), id: 0, stock_level: 0 },
  ],
};

export const fakeSearchResult = {
  id: 0,
  image: 'test',
  url: 'test',
  title: 'test',
}

export const fakeSearchError = {
  error: 'Could not find set 0 on Amazon',
};

export const fakeSearchSuccess = {
  result: fakeSearchResult
};


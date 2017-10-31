/* eslint-disable import/prefer-default-export */
export const fakeWatch = {
  id: 1,
  image: 'test',
  url: 'test',
  title: 'test',
  added: Date.now(),
  stock_levels: [
    { datetime: Date.now(), id: 1, stock_level: 0 },
  ],
};

export const fakeSearchResult = {
  id: 1,
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

export const fakeAddWatchSuccess = {
  result: fakeWatch
}

export const fakeAddWatchError = {
  error: 'Watch already exists for user'
}

export const fakeLocalStorageProfile = {
  getItem: () => JSON.stringify({
    email: 'test@test.com',
    token: '123',
  }),
};

export const fakeLocalStorageNoProfile = {
  getItem: () => null,
}

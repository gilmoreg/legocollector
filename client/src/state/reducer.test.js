import reducer from './reducer';
import * as actions from './actions';

const initialState = {
  loggedIn: false,
  email: '',
  token: '',
};

describe('Reducer', () => {
  it('should save an email and token on LOGIN', () => {
    const finalState = Object.assign({}, initialState,
      { loggedIn: true, email: 'test@test.com', token: '123' });
    expect(
      reducer(initialState, { type: actions.LOGIN, email: 'test@test.com', token: '123' })
    ).toEqual(finalState);
  });

  it('should clear loggedIn, email, and token on LOGOUT', () => {
    const finalState = Object.assign({}, initialState,
      { loggedIn: false, email: '', token: '' });
    const newState = reducer(initialState, actions.login({ email: 'test@test.com', token: '123' }));
    expect(
      reducer(newState, { type: actions.LOGOUT })
    ).toEqual(finalState);
  });

  it('should reset state on RESET', () => {
    // Change state with fake action to test reset
    const newState = reducer(initialState, actions.login({ email: 'test@test.com', token: '123' }));
    expect(
      reducer(newState, { type: actions.RESET })
    ).toEqual(initialState);
  });
});

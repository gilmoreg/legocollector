import reducer, { initialState } from './reducer';
import * as actions from './actions';
import { fakeWatch } from '../../utils/fakes';

describe('Reducer', () => {
  it('should return current state on unknown action', () => {
    expect(
      reducer(initialState, { type: 'UNKNOWN' })
    ).toEqual(initialState);
  });

  it('should fill watches on FILL_WATCHES', () => {
    const finalState = Object.assign({}, initialState, {
      watches: [fakeWatch, fakeWatch],
    });
    expect(
      reducer(initialState, { type: actions.FILL_WATCHES, watches: [fakeWatch, fakeWatch] }),
    ).toEqual(finalState);
  });

  it('should open the modal on OPEN_MODAL', () => {
    const finalState = Object.assign({}, initialState, { modalOpen: true });
    expect(
      reducer(initialState, { type: actions.OPEN_MODAL }),
    ).toEqual(finalState);
  });

  it('should close the modal on CLOSE_MODAL', () => {
    const finalState = Object.assign({}, initialState, { modalOpen: false });
    const midState = Object.assign({}, initialState, { modalOpen: true });
    expect(
      reducer(midState, { type: actions.CLOSE_MODAL }),
    ).toEqual(finalState);
  });

  it('should add a watch on ADD_WATCH', () => {
    const finalState = Object.assign({}, initialState, {
      watches: [ fakeWatch ]
    });
    expect(
      reducer(initialState, { type: actions.ADD_WATCH, watch: fakeWatch })
    ).toEqual(finalState);
  });

  it('should remove a watch on REMOVE_WATCH', () => {
    const startState = Object.assign({}, initialState, {
      watches: [fakeWatch],
    });
    expect(
      reducer(startState, { type: actions.REMOVE_WATCH, id: fakeWatch.id }),
    ).toEqual(initialState);
  });

  it('should save an email and token on LOGIN', () => {
    const finalState = Object.assign({}, initialState,
      { loggedIn: true, email: 'test@test.com', token: '123' });
    expect(
      reducer(initialState, { type: actions.LOGIN, email: 'test@test.com', token: '123' }),
    ).toEqual(finalState);
  });

  it('should clear loggedIn, email, and token on LOGOUT', () => {
    const finalState = Object.assign({}, initialState,
      { loggedIn: false, email: '', token: '' });
    const newState = reducer(initialState, actions.login({ email: 'test@test.com', token: '123' }));
    expect(
      reducer(newState, { type: actions.LOGOUT }),
    ).toEqual(finalState);
  });

  it('should reset state on RESET', () => {
    // Change state with fake action to test reset
    const newState = reducer(initialState, actions.login({ email: 'test@test.com', token: '123' }));
    expect(
      reducer(newState, { type: actions.RESET }),
    ).toEqual(initialState);
  });
});

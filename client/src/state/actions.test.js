import fetchMock from 'fetch-mock';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import * as actions from './actions';
import * as fakes from '../../utils/fakes';
import { initialState } from './reducer';

const mockStore = configureMockStore([thunk]);

describe('Action Creators', () => {
  it('should create an action to login', () => {
    const expectedAction = {
      type: actions.LOGIN,
      email: 'test@test.com',
      token: '123',
    };
    expect(actions.login({ email: 'test@test.com', token: '123' }))
      .toEqual(expectedAction);
  });

  it('should create an action to logout', () => {
    const expectedAction = {
      type: actions.LOGOUT,
    };
    expect(actions.logout()).toEqual(expectedAction);
  });

  it('should create an action to reset state', () => {
    const expectedAction = {
      type: actions.RESET,
    };
    expect(actions.reset()).toEqual(expectedAction);
  });

  it('should create an action to open the modal', () => {
    const expectedAction = {
      type: actions.OPEN_MODAL,
    };
    expect(actions.openModal()).toEqual(expectedAction);
  });

  it('should create an action to close the modal', () => {
    const expectedAction = {
      type: actions.CLOSE_MODAL,
    };
    expect(actions.closeModal()).toEqual(expectedAction);
  });

  it('should create an action to add a watch', () => {
    const expectedAction = {
      type: actions.ADD_WATCH,
      watch: fakes.fakeWatch,
    };
    expect(actions.addWatch(fakes.fakeWatch)).toEqual(expectedAction);
  });

  it('should create an action to fill watches', () => {
    const expectedAction = {
      type: actions.FILL_WATCHES,
      watches: [],
    };
    expect(actions.fillWatches([])).toEqual(expectedAction);
  });

  it('should create an action to remove a deleted watch', () => {
    const expectedAction = {
      type: actions.REMOVE_WATCH,
      id: 0,
    };
    expect(actions.removeWatch(0)).toEqual(expectedAction);
  });
});

describe('Async actions', () => {
  afterEach(() => {
    fetchMock.restore();
  });

  it('FETCH_WATCHES should dispatch FILL_WATCHES if successful', (done) => {
    fetchMock.mock(/.+\/watches.+/g,
      { result: [] },
    );
    const expectedActions = [
      { type: actions.FILL_WATCHES, watches: [] },
    ];
    
    const store = mockStore(initialState);
    store.dispatch(actions.fetchWatches('fakeToken'))
      .then(() => {
        const actualActions = store.getActions();
        expect(actualActions).toEqual(expectedActions);
        done();
      });
  });

  it('DELETE_WATCH should dispatch REMOVE_WATCH if successful', (done) => {
    fetchMock.mock(/.+\/watches.+/g,
      { result: 'Watch 12345 deleted' },
    );
    const expectedActions = [
      { type: actions.REMOVE_WATCH, id: 0 },
    ];
    const store = mockStore(initialState);
    store.dispatch(actions.deleteWatch('fakeToken', 0))
      .then(() => {
        const actualActions = store.getActions();
        expect(actualActions).toEqual(expectedActions);
        done();
      });
  });

  /* TODO ERROR TEST for FETCH_WATCHES and DELETE_WATCH */
});

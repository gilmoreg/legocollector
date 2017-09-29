import * as actions from './actions';

describe('Action Creators', () => {
  it('should create an action to login', () => {
    const expectedAction = {
      type: actions.LOGIN,
      email: 'test@test.com',
      accessToken: '123',
    };
    expect(actions.login({ email: 'test@test.com', accessToken: '123'}))
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
});

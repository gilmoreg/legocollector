// SYNC ACTIONS
export const LOGIN = 'LOGIN';
export const login = ({ email, accessToken }) => ({
  type: LOGIN,
  email,
  accessToken,
});

export const LOGOUT = 'LOGOUT';
export const logout = () => ({
  type: LOGOUT,
});

export const RESET = 'RESET';
export const reset = () => ({
  type: RESET,
});

// ASYNC ACTIONS
export const SET_THRESHOLD = 'SET_THRESHOLD';
export const setThreshold = ({ watch, level }) => dispatch =>
  null; // TODO update threshold via API

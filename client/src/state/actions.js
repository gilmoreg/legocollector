import { API_URL } from '../config';

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

export const FILL_WATCHES = 'FILL_WATCHES';
export const fillWatches = watches => ({
  type: FILL_WATCHES,
  watches,
});

// ASYNC ACTIONS
export const SET_THRESHOLD = 'SET_THRESHOLD';
export const setThreshold = ({ watch, level }) => (dispatch) => {
  // TODO update threshold via API
  console.log('setThreshold', watch, level);
};

export const FETCH_WATCHES = 'FETCH_WATCHES';
export const fetchWatches = ({ accessToken }) => dispatch =>
  fetch(`${API_URL}/api/watches?token=${accessToken}`)
    .then(res => res.json())
    .then(res => res.result)
    .then(watches => dispatch(fillWatches(watches)))
    .catch(err => console.error(err)); // TODO proper error handler

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

export const ADD_WATCH = 'ADD_WATCH';
export const addWatch = watch => ({
  type: ADD_WATCH,
  watch,
});

export const FILL_WATCHES = 'FILL_WATCHES';
export const fillWatches = watches => ({
  type: FILL_WATCHES,
  watches,
});

// ASYNC ACTIONS
export const SUBMIT_NEW_WATCH = 'SUBMIT_NEW_WATCH';
export const submitNewWatch = ({ setID, accessToken }) => dispatch =>
  fetch(`${API_URL}/api/watches/add`, {
    method: 'POST',
    body: JSON.stringify({
      token: accessToken,
      id: setID,
    }),
  })
    .then(res => res.json())
    .then(res => res.result)
    .then(watch => dispatch(addWatch(watch)))
    .catch(err => console.error(err)); // TODO proper error handler

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

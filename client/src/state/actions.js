import { API_URL } from '../config';
import { trimTitle } from '../regexes';

// SYNC ACTIONS
export const LOGIN = 'LOGIN';
export const login = ({ email, token }) => ({
  type: LOGIN,
  email,
  token,
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
  watch: Object.assign({}, watch, { title: trimTitle(watch.title)}),
});

export const FILL_WATCHES = 'FILL_WATCHES';
export const fillWatches = watches => ({
  type: FILL_WATCHES,
  watches: watches.map(watch => Object.assign({}, watch,
    { title: trimTitle(watch.title) }))
  });

export const REMOVE_WATCH = 'REMOVE_WATCH';
export const removeWatch = id => ({
  type: REMOVE_WATCH,
  id,
});

// ASYNC ACTIONS
export const FETCH_WATCHES = 'FETCH_WATCHES';
export const fetchWatches = token => dispatch =>
  fetch(`${API_URL}/watches?token=${token}`)
    .then(res => res.json())
    .then(res => res.result)
    .then(watches => dispatch(fillWatches(watches)))
    .catch(err => console.error(err)); // TODO proper error handler

export const DELETE_WATCH = 'DELETE_WATCH';
export const deleteWatch = (token, id) => dispatch =>
  fetch(`${API_URL}/watches/delete/${id}`, {
    method: 'POST',
    body: JSON.stringify({ token }),
  })
    .then(res => res.json())
    .then(res => res.result)
    .then(() => dispatch(removeWatch(id)))
    .catch(err => console.error(err)); // TODO proper error handler

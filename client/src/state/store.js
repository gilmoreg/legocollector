import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import reducer from './reducer';

let reduxDevtools;

if (typeof window !== 'undefined') {
  reduxDevtools = window.__REDUX_DEVTOOLS_EXTENSION__
  && window.__REDUX_DEVTOOLS_EXTENSION__();
} else {
  reduxDevtools = global.__REDUX_DEVTOOLS_EXTENSION__ &&
  global.__REDUX_DEVTOOLS_EXTENSION__();
}

export default createStore(reducer,
  reduxDevtools,
  applyMiddleware(thunk),
);

import * as actions from './actions';

export const initialState = {
  loggedIn: false,
  email: '',
  token: '',
};

export default function reducer(state = initialState, action) {
  console.log(action);
  switch (action.type) {
    case actions.LOGIN: {
      return Object.assign({}, state,
        { loggedIn: true, email: action.email, token: action.token },
      );
    }
    case actions.LOGOUT: {
      return Object.assign({}, state,
        { loggedIn: false, email: '', token: '' },
      );
    }
    case actions.RESET: {
      return initialState;
    }
    default: return state;
  }
}

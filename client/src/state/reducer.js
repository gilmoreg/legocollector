import * as actions from './actions';

export const initialState = {
  loggedIn: false,
  email: '',
  token: '',
  watches: [],
  modalOpen: false,
};

export default function reducer(state = initialState, action) {
  console.log(action);
  switch (action.type) {
    case actions.OPEN_MODAL: {
      return Object.assign({}, state, { modalOpen: true });
    }
    case actions.CLOSE_MODAL: {
      return Object.assign({}, state, { modalOpen: false });
    }
    case actions.ADD_WATCH: {
      return Object.assign({}, state, { watches: [...state.watches, action.watch] });
    }
    case actions.FILL_WATCHES: {
      return Object.assign({}, state, { watches: action.watches });
    }
    case actions.REMOVE_WATCH: {
      const watches = state.watches.filter(watch => (watch.id !== action.id));
      return Object.assign({}, state, { watches });
    }
    case actions.LOGIN: {
      return Object.assign({}, state,
        { loggedIn: true, email: action.email, token: action.token },
      );
    }
    case actions.LOGOUT: {
      return initialState;
    }
    case actions.RESET: {
      return initialState;
    }
    default: return state;
  }
}

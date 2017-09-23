import * as actions from './actions';

const initialState = {};

export default function reducer(state = initialState, action) {
  console.log(action);
  switch (action.type) {
    case actions.RESET: {
      return initialState;
    }
    default: return state;
  }
}

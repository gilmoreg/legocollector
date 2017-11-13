import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './state/store';
import './index.css';
import App from './components/App';
import AddWatchModal from './components/AddWatch/AddWatchModal';
import { API_URL } from './config';
import registerServiceWorker from './registerServiceWorker';

document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <Provider store={store}>
      <div className='container'>
        <App />
        <AddWatchModal />
      </div>
    </Provider>,
    document.getElementById('root'),
  );
});
registerServiceWorker();
// Wake up Heroku asap - don't need to process the response
fetch(`${API_URL}/`);
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './styles.css';
import UserProvider from './context/UserContext';

const root = createRoot(document.getElementById('root') as HTMLElement);

root.render(
  <React.StrictMode>
    <UserProvider>
      <App />
    </UserProvider>
  </React.StrictMode>
);

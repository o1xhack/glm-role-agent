// src/App.tsx
import React from 'react';
import { ThemeProvider } from 'styled-components';
import { theme } from './styles/theme';
import HomePage from './pages/HomePage';

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <div>
        <HomePage />
      </div>
    </ThemeProvider>
  );
}

export default App;
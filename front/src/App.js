import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './views/Login';
import CreditList from './components/CreditList';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(localStorage.getItem('access') !== null);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setIsLoggedIn(false);
  };

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route 
            path="/" 
            element={isLoggedIn ? <Navigate to="/credits" /> : <Login onLogin={handleLogin} />} 
          />
          <Route 
            path="/credits" 
            element={isLoggedIn ? <CreditList onLogout={handleLogout} /> : <Navigate to="/" />} 
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

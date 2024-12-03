import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './views/Login';
import CreditList from './components/CreditList';
import ProductList from './components/ProductList';
import ClientList from './components/ClientList';
import Sidebar from './components/SideBar';

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
        {isLoggedIn && <Sidebar onLogout={handleLogout} />}
        <div className="content" style={{ marginLeft: isLoggedIn ? '220px' : '0' }}>
          <Routes>
            <Route 
              path="/" 
              element={isLoggedIn ? <Navigate to="/credits" /> : <Login onLogin={handleLogin} />} 
            />
            <Route 
              path="/credits" 
              element={isLoggedIn ? <CreditList /> : <Navigate to="/" />} 
            />
            <Route 
              path="/products" 
              element={isLoggedIn ? <ProductList /> : <Navigate to="/" />} 
            />
            <Route 
              path="/clients" 
              element={isLoggedIn ? <ClientList /> : <Navigate to="/" />} 
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;

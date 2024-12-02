import React, { useState } from 'react';
import Login from './views/Login';
import CreditList from './components/CreditList';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  return (
    <div className="App">
      {isLoggedIn ? <CreditList /> : <Login onLogin={handleLogin} />}
    </div>
  );
}

export default App;

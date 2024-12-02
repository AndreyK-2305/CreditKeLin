import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CreditList = () => {
  const [credits, setCredits] = useState([]);
  const [error, setError] = useState('');

  const fetchCredits = async () => {
    try {
      const token = localStorage.getItem('access');
      if (!token) {
        throw new Error('No token found');
      }
      console.log('Fetching credits with token:', token); // Depuración
      const response = await axios.get('http://localhost:8000/api/credits/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setCredits(response.data);
    } catch (error) {
      console.error('Error fetching credits:', error); // Depuración
      if (error.response && error.response.data.code === 'token_not_valid') {
        console.log('Token not valid, attempting to refresh'); // Depuración
        await refreshAccessToken();
        fetchCredits(); // Volver a intentar obtener los créditos
      } else {
        setError('Error fetching credits');
      }
    }
  };

  const refreshAccessToken = async () => {
    try {
      const refresh = localStorage.getItem('refresh');
      if (!refresh) {
        throw new Error('No refresh token found');
      }
      console.log('Refreshing access token with refresh token:', refresh); // Depuración
      const response = await axios.post('http://localhost:8000/api/token/refresh/', {
        refresh: refresh,
      });
      localStorage.setItem('access', response.data.access);
      console.log('Access token refreshed'); // Depuración
    } catch (error) {
      console.error('Error refreshing access token:', error); // Depuración
      setError('Error refreshing access token');
    }
  };

  useEffect(() => {
    fetchCredits();
  }, []);

  return (
    <div>
      <h2>List of Credits</h2>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <ul>
        {credits.map(credit => (
          <li key={credit.id}>{credit.name} - {credit.amount}</li>
        ))}
      </ul>
    </div>
  );
};

export default CreditList;

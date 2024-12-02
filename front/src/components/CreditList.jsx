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
      const response = await axios.get('http://localhost:8000/api/credits/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setCredits(response.data);
    } catch (error) {
      if (error.response && error.response.data.code === 'token_not_valid') {
        // Intentar actualizar el token de acceso
        await refreshAccessToken();
        fetchCredits(); // Volver a intentar obtener los créditos
      } else {
        setError('Error fetching credits');
        console.error('There was an error fetching credits!', error);
      }
    }
  };

  const refreshAccessToken = async () => {
    try {
      const refresh = localStorage.getItem('refresh');
      const response = await axios.post('http://localhost:8000/api/token/refresh/', {
        refresh: refresh,
      });
      localStorage.setItem('access', response.data.access);
    } catch (error) {
      setError('Error refreshing access token');
      console.error('There was an error refreshing access token!', error);
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

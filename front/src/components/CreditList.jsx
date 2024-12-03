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
      console.log('Credits data received:', response.data); // Depuración
    } catch (error) {
      console.error('Error fetching credits:', error); // Depuración
      setError('Error fetching credits');
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
          <li key={credit.id}>
            <p><strong>Client Name:</strong> {credit.client_name}</p>
            <p><strong>Product Name:</strong> {credit.product_name}</p>
            <p><strong>Status:</strong> {credit.status}</p>
            <p><strong>Debt:</strong> {credit.debt}</p>
            <p><strong>Total Payments:</strong> {credit.total_payments}</p>
            <h4>Payments:</h4>
            <ul>
              {credit.payments.map(payment => (
                <li key={payment.id}>
                  <p><strong>Value:</strong> {payment.value}</p>
                  <p><strong>Delayed Value:</strong> {payment.delayed_value}</p>
                  <p><strong>Status:</strong> {payment.payment_STATUS}</p>
                  <p><strong>Due To:</strong> {payment.due_to}</p>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CreditList;

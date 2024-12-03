import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Modal from './Modal';
import './styles/CreditList.css'; // Importar el archivo CSS

const CreditList = () => {
  const [credits, setCredits] = useState([]);
  const [error, setError] = useState('');
  const [selectedCredit, setSelectedCredit] = useState(null);
  const [showModal, setShowModal] = useState(false);

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

  const handleCreditClick = (credit) => {
    console.log('Selected Credit:', credit); // Depuración
    console.log('Payments:', credit.payments); // Depuración
    setSelectedCredit(credit);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  useEffect(() => {
    fetchCredits();
  }, []);

  return (
    <div className="credit-list">
      <h2>Credit List</h2>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <ul>
        {credits.map(credit => (
          <li key={credit.id} onClick={() => handleCreditClick(credit)}>
            <p><strong>Client:</strong> {credit.client_name}</p>
            <p><strong>Product:</strong> {credit.product_name}</p>
            <p><strong>Status:</strong> {credit.status}</p>
            <p><strong>Debt:</strong> {credit.debt}</p>
            <p><strong>Total Payments:</strong> {credit.total_payments}</p>
          </li>
        ))}
      </ul>
      {selectedCredit && (
        <Modal show={showModal} onClose={handleCloseModal} credit={selectedCredit} />
      )}
    </div>
  );
};

export default CreditList;

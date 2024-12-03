import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/CreditList.css'; // Reutilizar el mismo archivo CSS

const ClientList = () => {
  const [clients, setClients] = useState([]);
  const [error, setError] = useState('');
  const [selectedClient, setSelectedClient] = useState(null);
  const [credits, setCredits] = useState([]);

  const fetchClients = async () => {
    try {
      const token = localStorage.getItem('access');
      if (!token) {
        throw new Error('No token found');
      }
      console.log('Fetching clients with token:', token); // Depuración
      const response = await axios.get('http://localhost:8000/api/users/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setClients(response.data);
      console.log('Clients data received:', response.data); // Depuración
    } catch (error) {
      console.error('Error fetching clients:', error); // Depuración
      setError('Error fetching clients');
    }
  };

  const fetchCredits = async (clientId) => {
    try {
      const token = localStorage.getItem('access');
      if (!token) {
        throw new Error('No token found');
      }
      console.log(`Fetching credits for client ${clientId} with token:`, token); // Depuración
      const response = await axios.get(`http://localhost:8000/clients/${clientId}/credits/`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setCredits(response.data);
      console.log(`Credits data for client ${clientId} received:`, response.data); // Depuración
    } catch (error) {
      console.error(`Error fetching credits for client ${clientId}:`, error); // Depuración
      setError('Error fetching credits');
    }
  };

  const handleClientClick = (client) => {
    console.log('Selected Client:', client); // Depuración
    setSelectedClient(client);
    fetchCredits(client.id);
  };

  useEffect(() => {
    fetchClients();
  }, []);

  return (
    <div className="credit-list">
      <h2>List of Clients</h2>
      {error && <div className="error">{error}</div>}
      <ul>
        {clients.map(client => (
          <li key={client.id} onClick={() => handleClientClick(client)}>
            <p><strong>Name:</strong> {client.name}</p>
            <p><strong>Email:</strong> {client.email}</p>
            <p><strong>Phone:</strong> {client.telefono}</p>
          </li>
        ))}
      </ul>
      {selectedClient && (
        <div className="credit-list">
          <h3>Credits for {selectedClient.name}</h3>
          <ul>
            {credits.map(credit => (
              <li key={credit.id}>
                <p><strong>Product:</strong> {credit.product_name}</p>
                <p><strong>Status:</strong> {credit.status}</p>
                <p><strong>Debt:</strong> {credit.debt}</p>
                <p><strong>Total Payments:</strong> {credit.total_payments}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ClientList;

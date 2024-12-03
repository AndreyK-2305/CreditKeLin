import React from 'react';
import './styles/Modal.css'; // Archivo CSS para estilizar el modal

const Modal = ({ show, onClose, credit }) => {
  if (!show || !credit) {
    return null;
  }

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="close-button" onClick={onClose}>X</button>
        <h2>Payments for {credit.client_name}</h2>
        {credit.payments && credit.payments.length > 0 ? (
          <ul>
            {credit.payments.map(payment => (
              <li key={payment.id}>
                <p><strong>Value:</strong> {payment.value}</p>
                <p><strong>Delayed Value:</strong> {payment.delayed_value}</p>
                <p><strong>Status:</strong> {payment.payment_STATUS}</p>
                <p><strong>Date:</strong> {payment.due_to}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No payments found.</p>
        )}
      </div>
    </div>
  );
};

export default Modal;

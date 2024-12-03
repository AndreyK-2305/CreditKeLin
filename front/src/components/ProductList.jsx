import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/CreditList.css';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState('');

  const fetchProducts = async () => {
    try {
      const token = localStorage.getItem('access');
      if (!token) {
        throw new Error('No token found');
      }
      console.log('Fetching products with token:', token); // Depuración
      const response = await axios.get('http://localhost:8000/api/products/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      setProducts(response.data);
      console.log('Products data received:', response.data); // Depuración
    } catch (error) {
      console.error('Error fetching products:', error); // Depuración
      setError('Error fetching products');
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div className="credit-list"> 
      <h2>List of Products</h2>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <p><strong>Product Name:</strong> {product.product_name}</p>
            <p><strong>Price:</strong> {product.price}</p>
            <p><strong>Available:</strong> {product.available}</p>
            <p><strong>Description:</strong> {product.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
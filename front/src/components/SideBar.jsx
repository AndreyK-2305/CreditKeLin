import React from 'react';
import { NavLink } from 'react-router-dom';
import './styles/SideBar.css';

const Sidebar = ({ onLogout }) => {
  return (
    <div className="sidebar">
      <h2>Navigation</h2>
      <ul>
        <li>
          <NavLink to="/credits" activeClassName="active">
            Credits
          </NavLink>
        </li>
        <li>
          <NavLink to="/products" activeClassName="active">
            Products
          </NavLink>
        </li>
        <li>
          <NavLink to="/clients" activeClassName="active">
            Clients
          </NavLink>
        </li>
      </ul>
      <button className="logout-button" onClick={onLogout}>Logout</button>
    </div>
  );
};

export default Sidebar;
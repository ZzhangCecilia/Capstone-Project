import React from 'react';
import RegisterForm from './components/RegisterForm';
import ProductList from './components/ProductList';

function App() {
  return (
    <div className="container mt-4">
      <h1>ReMarket</h1>
      <RegisterForm />
      <ProductList />
    </div>
  );
}

export default App;


// Lab 1–3: This is the root component that renders the overall layout of the ReMarket application.
import React, { useState } from 'react';
import ProductList from './components/ProductList';
import RegisterForm from './components/RegisterForm';

function App() {
  // Lab 2: Define a sample product list to pass as props to the ProductList component
  const [products] = useState([
    { name: 'Desk Lamp', price: 10 },
    { name: 'Office Chair', price: 25 },
    { name: 'Used Textbook', price: 15 },
    { name: 'Monitor Stand', price: 20 },
    { name: 'Bluetooth Keyboard', price: 18 },
  ]);

  return (
    <div className="container mt-4">
      {/* Lab 1: Title and layout container */}
      <h1>ReMarket</h1>

      {/* Lab 3: User registration form component */}
      <RegisterForm />

      {/* Lab 2: Product list component */}
      <ProductList products={products} />
    </div>
  );
}

export default App;



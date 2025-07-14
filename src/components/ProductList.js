import React, { useEffect, useState } from 'react';

// Lab 2: Product listing with API fetch
const ProductList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5050/api/products')
      .then(res => res.json())
      .then(data => {
      console.log("Fetched products:", data); 
      setItems(data);
    })
      .catch(err => console.error('Error fetching items:', err));
  }, []);

  return (
    <div className="p-4">
      <h2>Available Items</h2>
      <ul className="list-group">
        {items.map(item => (
          <li className="list-group-item" key={item.id}>
            {item.name} - ${item.price}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;

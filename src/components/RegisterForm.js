import React, { useState } from 'react';

const RegisterForm = () => {
  // State variables to store user input for email and password
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState(''); // State to store feedback message

  // Function to handle registration when the user clicks the button
  const handleRegister = async () => {
    try {
      // Send a POST request to the Flask backend
      const response = await fetch('http://127.0.0.1:5050/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        // Include email and password in the request body
        body: JSON.stringify({ email, password }),
      });

      // Parse the JSON response
      const result = await response.json();

      // Display the returned message
      setMessage(result.message);
    } catch (error) {
      // Show error message if the request fails
      console.error('Registration failed:', error);
      setMessage('Registration failed. Please try again.');
    }
  };

  return (
    <div>
      <h2>Register with your .edu email</h2>
      {/* Input field for email */}
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <br />
      {/* Input field for password */}
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br />
      {/* Button to trigger registration */}
      <button onClick={handleRegister}>Register</button>
      {/* Show message from backend */}
      {message && <p>{message}</p>}
    </div>
  );
};

export default RegisterForm;



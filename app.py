from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Dummy product data
products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Coffee Maker", "price": 49},
    {"id": 3, "name": "Desk Lamp", "price": 19},
    {"id": 4, "name": "Bookshelf", "price": 59},
    {"id": 5, "name": "Office Chair", "price": 89}
]

# In-memory list to store registered users
users = []

# API endpoint to return product list
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# API endpoint to register a new user
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Basic validation
    if not email or not password or not email.endswith('.edu'):
        return jsonify({'message': 'Invalid email or password'}), 400

    # Check if user already exists
    for user in users:
        if user['email'] == email:
            return jsonify({'message': 'User already exists'}), 409

    # Hash password and save user
    hashed_password = generate_password_hash(password)
    users.append({'email': email, 'password': hashed_password})

    return jsonify({'message': 'User registered successfully'}), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)





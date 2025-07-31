import datetime
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import db, User

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/api')

# ===========================
# Register a new user
# ===========================
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check for missing fields
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    # Hash the password and create a new user
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)

    # Save to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# ===========================
# User login and token issue
# ===========================
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Query user from database
    user = User.query.filter_by(username=username).first()

    # Check credentials
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200

# ===========================
# Protected route to get user info
# ===========================
@auth_bp.route('/info', methods=['GET'])
@jwt_required()
def info():
    current_user_id = get_jwt_identity()
    return jsonify({"user_id": current_user_id}), 200






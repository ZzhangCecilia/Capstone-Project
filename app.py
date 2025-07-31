# Lab 1: Initialize Flask backend
# This sets up a minimal Flask app that can serve API responses to the frontend.
from flask import Flask, request, jsonify
from flask_cors import CORS
from app.routes.auth import auth_bp
from app.routes.items import items_bp
from app.routes.order import order_bp
from app.models import db
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Configure PostgreSQL database (update with your actual password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/remarket'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Register blueprints for different route modules
app.register_blueprint(auth_bp)
app.register_blueprint(items_bp)
app.register_blueprint(order_bp)

# Enable CORS for frontend-backend communication
from flask_cors import CORS

CORS(app, resources={r"/api/*": {"origins": "*"}})


# Create tables and run the app
from app import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables defined in models.py

    app.run(debug=True, host='0.0.0.0', port=5050)






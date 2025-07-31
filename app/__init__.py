# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/remarket'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from .models import User, Item, Order
    with app.app_context():
        db.create_all()

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.items import items_bp
    from app.routes.order import order_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(order_bp)

    return app



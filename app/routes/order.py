# routes/order.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Order, Item

# Blueprint for order routes
order_bp = Blueprint('orders', __name__, url_prefix='/api')

@orders_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    item_id = data.get('item_id')
    quantity = data.get('quantity')

    if not item_id or not quantity:
        return jsonify({'error': 'Missing item_id or quantity'}), 400

    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    current_user_id = get_jwt_identity()
    new_order = Order(
        buyer_id=current_user_id,
        item_id=item_id,
        quantity=quantity,
        total_price=item.price * quantity
    )
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 201

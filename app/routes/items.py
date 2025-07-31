# app/routes/items.py
from flask import Blueprint, request, jsonify
from app.models import db, Item
from flask_jwt_extended import jwt_required, get_jwt_identity

items_bp = Blueprint('items', __name__)

@items_bp.route('/api/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')
    category = data.get('category')
    image_url = data.get('image_url')

    seller_id = get_jwt_identity()

    new_item = Item(
        title=title,
        description=description,
        price=price,
        category=category,
        image_url=image_url,
        seller_id=seller_id
    )

    print("Item created:", new_item.title)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({"message": "Item created successfully."}), 201

@items_bp.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    result = []
    for item in items:
        result.append({
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": str(item.price),
            "category": item.category,
            "image_url": item.image_url,
            "seller_id": item.seller_id
        })
    return jsonify(result), 200

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()

    items_list = [dict(item) for item in items]
    return jsonify(items_list), 200


@app.route('/api/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')
    category = data.get('category')
    image_url = data.get('image_url')

    user_id = get_jwt_identity()

    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,)).fetchone()
    if item is None:
        conn.close()
        return jsonify({'error': 'Item not found'}), 404
    if item['seller_id'] != user_id:
        conn.close()
        return jsonify({'error': 'Unauthorized'}), 403

    conn.execute("""
        UPDATE items SET 
            title = ?, 
            description = ?, 
            price = ?, 
            category = ?, 
            image_url = ?
        WHERE id = ?
    """, (title, description, price, category, image_url, item_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Item updated successfully'}), 200


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    user_id = get_jwt_identity()

    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,)).fetchone()
    if item is None:
        conn.close()
        return jsonify({'error': 'Item not found'}), 404
    if item['seller_id'] != user_id:
        conn.close()
        return jsonify({'error': 'Unauthorized'}), 403

    conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Item deleted successfully'}), 200



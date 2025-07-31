# 📘 ReMarket API Documentation

# ----------------------------
#  USERS
# ----------------------------

# [POST] /api/register
# Description: Register a new user
# Request Body:
# {
#   "username": "alice",
#   "email": "alice@example.com",
#   "password": "mypassword"
# }
# Response:
# {
#   "message": "User registered successfully"
# }

# [POST] /api/login
# Description: Log in a user and receive JWT token
# Request Body:
# {
#   "email": "alice@example.com",
#   "password": "mypassword"
# }
# Response:
# {
#   "token": "your-jwt-token"
# }

# [GET] /api/info
# Description: Get current user info
# Headers:
#   Authorization: Bearer <token>
# Response:
# {
#   "id": 1,
#   "username": "alice",
#   "email": "alice@example.com"
# }

# ----------------------------
# ITEMS
# ----------------------------

# [GET] /api/items
# Description: Get all items
# Headers:
#   Authorization: Bearer <token>
# Response:
# [
#   {
#     "id": 1,
#     "title": "Backpack",
#     "description": "Black hiking backpack",
#     "price": 25.0,
#     "user_id": 1
#   }
# ]

# [POST] /api/items
# Description: Create a new item
# Headers:
#   Authorization: Bearer <token>
# Request Body:
# {
#   "title": "Desk Lamp",
#   "description": "Bright LED lamp",
#   "price": 15.0
# }
# Response:
# {
#   "message": "Item created successfully",
#   "item": {
#     "id": 2,
#     "title": "Desk Lamp",
#     "description": "Bright LED lamp",
#     "price": 15.0,
#     "user_id": 1
#   }
# }

# [PUT] /api/items/<item_id>
# Description: Update an existing item
# Headers:
#   Authorization: Bearer <token>
# Request Body:
# {
#   "title": "Updated Lamp",
#   "description": "Updated description",
#   "price": 18.0
# }
# Response:
# {
#   "message": "Item updated successfully"
# }

# [DELETE] /api/items/<item_id>
# Description: Delete an item
# Headers:
#   Authorization: Bearer <token>
# Response:
# {
#   "message": "Item deleted successfully"
# }

# ----------------------------
# ORDERS
# ----------------------------

# [GET] /api/orders
# Description: Get all orders of current user
# Headers:
#   Authorization: Bearer <token>
# Response:
# [
#   {
#     "id": 1,
#     "item_id": 2,
#     "quantity": 1,
#     "total_price": 15.0,
#     "user_id": 1
#   }
# ]

# [POST] /api/orders
# Description: Create a new order
# Headers:
#   Authorization: Bearer <token>
# Request Body:
# {
#   "item_id": 2,
#   "quantity": 1
# }
# Response:
# {
#   "message": "Order created successfully",
#   "order": {
#     "id": 1,
#     "item_id": 2,
#     "quantity": 1,
#     "total_price": 15.0,
#     "user_id": 1
#   }
# }

# [PUT] /api/orders/<order_id>
# Description: Update an order quantity
# Headers:
#   Authorization: Bearer <token>
# Request Body:
# {
#   "quantity": 2
# }
# Response:
# {
#   "message": "Order updated successfully"
# }

# [DELETE] /api/orders/<order_id>
# Description: Delete an order
# Headers:
#   Authorization: Bearer <token>
# Response:
# {
#   "message": "Order deleted successfully"
# }

# ----------------------------
# NOTES
# ----------------------------
# - All endpoints except register/login require JWT token in Authorization header.
# - Example: Authorization: Bearer <your-token>
# - Only the owner can create, view, update, or delete their own items and orders.
# - Order total_price = quantity * item.price

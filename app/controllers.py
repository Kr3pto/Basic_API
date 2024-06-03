from app import app
from flask import jsonify, request
from app.models import User

# user predefined params
users = [
    User(1, "Alice"),
    User(2, "Bob"),
    User(3, "Charlie")
]

# checks if user is in the predefined param and gives a code 
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user.user_id == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())

# adds a new user in the post reuest
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(user_id=len(users) + 1, username=data['username'])
    users.append(new_user)
    return jsonify(new_user.to_dict()), 201

from flask import Blueprint, request, jsonify
from models import User
from extensions import db
from flask_jwt_extended import create_access_token, jwt_required

# Define a blueprint for authentication-related routes
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Endpoint to register a new user
    data = request.get_json()

    if len(data['username']) < 10:
        return jsonify({"error": "Username must be at least 10 characters long"}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Endpoint for user login
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.id)
        return jsonify(token=token), 200
    return jsonify({"error": "Invalid username or password"}), 401

@auth_bp.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    # Admin-only route
    return jsonify({"message": "Welcome, admin!"}), 200

@auth_bp.route('/crud/<username>', methods=['GET'])
@jwt_required()
def crud(username):
    # Get user data by username
    data = request.args
    user = User.query.filter_by(username=username).first()
    print(user)
    return jsonify({"token": user.password_hash, "user_id": user.id}), 200

    
@auth_bp.route('/crudd/<id>', methods=['DELETE'])
@jwt_required()
def crudd(id):
     # Delete a user by ID
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"Status": "User has been deleted"}),200

@auth_bp.route('/cruddd/<id>', methods=['PATCH'])
@jwt_required()
def cruddd(id):
    # Update a user's username
    data = request.json
    user = User.query.filter_by(id=id).first()
    user.username = data["new_username"]
    db.session.commit()
    return jsonify({"Status": "User has been Updated"}),200
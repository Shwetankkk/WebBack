from flask import Blueprint, jsonify
from models import User

# Define a blueprint for public routes
public_bp = Blueprint('public_bp', __name__)

@public_bp.route('/public', methods=['GET'])
def public_route():
    # Retrieve all usernames from the User model
    usernames = [user.username for user in User.query.all()]
    return jsonify(usernames), 200



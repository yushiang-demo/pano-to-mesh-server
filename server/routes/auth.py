from flask import Blueprint, request, jsonify
from models.user import User
from app.extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signup", methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first() is not None:
        return {
            'error_code': 400001,
            'message': 'member already existed.'
        }, 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return { 
        'data': { 
            'username': username 
        } 
    }, 200
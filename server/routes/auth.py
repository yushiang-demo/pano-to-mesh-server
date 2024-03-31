from flask import Blueprint
from models.user import User
from app.extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/")
def hello():
    return "Hello, World!"
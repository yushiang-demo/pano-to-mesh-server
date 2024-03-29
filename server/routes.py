from flask import Blueprint
from models.user import User
from extensions import db

api_bp = Blueprint('api', __name__)

@api_bp.route("/")
def hello():
    return "Hello, World!"
from flask import Flask
from .extensions import db
from .config import config
from routes.auth import auth_bp
 
def create_app(config_name):
 
    app = Flask(__name__)
    app.app_context().push()

    app.config.from_object(config[config_name])
    db.init_app(app)

    app.register_blueprint(auth_bp)

    return app
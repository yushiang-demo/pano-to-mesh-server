import os
from flask import Flask
from routes import api_bp
from extensions import db
from flask_migrate import Migrate

app = Flask(__name__)
app.app_context().push()

app.register_blueprint(api_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
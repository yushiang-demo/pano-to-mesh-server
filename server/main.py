import os
from app.extensions import db
from app import create_app
from flask_migrate import Migrate

app = create_app('development')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
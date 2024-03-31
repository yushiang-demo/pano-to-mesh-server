import os
 
basedir = os.path.abspath(os.path.dirname(__file__))

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)
 
class BaseConfig:
    SECRET_KEY = 'SECRET_KEY'
 
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')
 
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")
 
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
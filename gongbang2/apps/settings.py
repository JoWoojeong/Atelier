"""
settings.py

Configuration for Flask app

"""
from datetime import timedelta

class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "tkdwnsdigh@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///gongbang?instance=likelion3:dbtest1'
    migration_directory = 'migrations'


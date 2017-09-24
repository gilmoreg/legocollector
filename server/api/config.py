'''
  Configuration
'''
import os

DEBUG = True
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = 'keyboard puma'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

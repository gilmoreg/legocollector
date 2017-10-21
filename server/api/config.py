"""
  Configuration
"""
import os


class Config(object):
    """ Base configuration """
    SECRET_KEY = os.environ['JWT_SECRET']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ['RABBITMQ_URL']
    CSRF_ENABLED = True
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    DEBUG = False


class ProdConfig(Config):
    """ Production config """
    ENV = 'prod'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """ Development config """
    ENV = 'dev'
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    """ Testing config """
    ENV = 'dev'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

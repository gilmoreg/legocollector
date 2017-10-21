"""
  Configuration
"""
import os
from celery.schedules import crontab


class Config(object):
    """ Base configuration """
    SECRET_KEY = os.environ['JWT_SECRET']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ['RABBITMQ_URL']
    CSRF_ENABLED = True
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory


class ProdConfig(Config):
    """ Production config """
    ENV = 'prod'
    DEBUG = False
    TESTING = False
    CELERYBEAT_SCHEDULE = {
        'update': {
            'task': 'update_stock_levels',
            'schedule': crontab(hour=0, minute=0)
        }
    }


class DevConfig(Config):
    """ Development config """
    ENV = 'dev'
    DEBUG = True
    TESTING = False
    CELERYBEAT_SCHEDULE = {
        'update': {
            'task': 'update_stock_levels',
            'schedule': crontab(minute='*')
        }
    }


class TestConfig(Config):
    """ Testing config """
    ENV = 'dev'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

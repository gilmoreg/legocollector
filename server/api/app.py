"""
    Factory functions for setup
"""
from flask import Flask, jsonify
from flask_cors import CORS
from celery import Celery
from os import environ

import api.views as views
from api.config import ProdConfig
from api.database import db
from api.errors import FlaskError
from api.controllers.legoset_controller import LegoSetController

celery = Celery(__name__, broker=environ['RABBITMQ_URL'])


def create_app(config_object=ProdConfig):
    """ Factory function for creating application object """
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app, support_credentials=True)
    db.init_app(app)
    celery.conf.update(app.config)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_blueprints(app):
    """ Register blueprints """
    app.register_blueprint(views.legoset.blueprint)
    app.register_blueprint(views.login.blueprint)
    app.register_blueprint(views.watches.blueprint)


def register_errorhandlers(app):
    """ Register error handlers """
    @app.errorhandler(FlaskError)
    def handle_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

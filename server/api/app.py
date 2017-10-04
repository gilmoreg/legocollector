'''
    Factory functions for setup
'''
from flask import Flask
from flask_cors import CORS
from api.database import db
import api.views as views


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app, support_credentials=True)
    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(views.legoset.blueprint)
    app.register_blueprint(views.login.blueprint)
    app.register_blueprint(views.watches.blueprint)


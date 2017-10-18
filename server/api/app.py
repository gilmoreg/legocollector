'''
    Factory functions for setup
'''
from flask import Flask, jsonify, g
from flask_cors import CORS
from api.config import ProdConfig
from api.database import db
import api.views as views
from api.errors import FlaskError
from api.schedule import update_stock_levels


def create_app(config_object=ProdConfig):
    ''' Factory function for creating application object '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app, support_credentials=True)
    db.init_app(app)
    register_blueprints(app)
    register_errorhandlers(app)
    # update_stock_levels(app)
    return app


def register_blueprints(app):
    ''' Register blueprints '''
    app.register_blueprint(views.legoset.blueprint)
    app.register_blueprint(views.login.blueprint)
    app.register_blueprint(views.watches.blueprint)


def register_errorhandlers(app):
    ''' Register error handlers '''
    @app.errorhandler(FlaskError)
    def handle_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

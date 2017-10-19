"""
    Database migrations script

    Usage:
    export FLASK_APP=/src/migrate.py
    flask db init
    flask db migrate
    flask db upgrade
"""
from api.app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.database import db
import api.models

flask_app = create_app()
migrate = Migrate(flask_app, db)

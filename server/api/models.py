'''
  Model definitions
'''
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_migrate import Migrate
from api import app

# Initialize database connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
        Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, dt.date)
            else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class LegoSet(BaseModel):
    '''
    Model for watched Lego set
    '''
    __tablename__ = 'legoset'
    # Equal to the official lego Set Number
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))
    url = db.Column(db.String(255))
    added = db.Column(db.DateTime)
    stock_levels = db.relationship('StockLevel',
                                   backref='stock_levels_legoset',
                                   lazy='dynamic')
    watches = db.relationship('Watch', backref='watches_legoset',
                              lazy='dynamic')

    def __init__(self, lego_set):
        self.id = lego_set['id']
        self.title = lego_set['title']
        self.image = lego_set['image']
        self.url = lego_set['url']
        self.added = dt.utcnow()


class Watch(BaseModel):
    '''
    Stores mapping from User to LegoSet
    Indicating this user watches this set
    '''
    __tablename__ = 'watch'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    lego_set = db.Column(db.Integer, db.ForeignKey('legoset.id'))
    added = db.Column(db.DateTime)

    def __init__(self, user, lego_set):
        self.user = user
        self.lego_set = lego_set
        self.added = dt.utcnow()


class User(BaseModel):
    '''
    Model for User
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    added = db.Column(db.DateTime)
    watches = db.relationship('Watch', backref='watches_user', lazy='dynamic')

    def __init__(self, email):
        self.email = email
        self.added = dt.utcnow()


class StockLevel(BaseModel):
    '''
    Model storing a stock level datapoint
    '''
    __tablename__ = 'stocklevel'
    id = db.Column(db.Integer, primary_key=True)
    lego_set = db.Column(db.Integer, db.ForeignKey('legoset.id'))
    datetime = db.Column(db.DateTime)
    stock_level = db.Column(db.Integer)

    def __init__(self, lego_set, stock_level):
        self.lego_set = lego_set
        self.stock_level = stock_level
        self.datetime = dt.utcnow()
'''
  Model definitions
'''
from api.database import db
from datetime import datetime as dt


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self.to_dict().items()
        })


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
    '''
    Establishes a collection of StockLevel objects on LegoSet
    called LegoSet.stock_levels
    Also establishes a .legoset attribute on StockLevel
    which refers to the parent LegoSet

    When creating a StockLevel object, call
    legoset.stock_levels.append(stock_level)
    '''
    stock_levels = db.relationship('StockLevel',
                                   back_populates='legoset',
                                   lazy='dynamic')

    def __init__(self, legoset):
        self.id = legoset['id']
        self.title = legoset['title']
        self.image = legoset['image']
        self.url = legoset['url']
        self.added = dt.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'url': self.url,
            'added': self.added
        }


class Watch(BaseModel):
    '''
    Stores mapping from User to LegoSet
    Indicating this user watches this set
    '''
    __tablename__ = 'watch'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    added = db.Column(db.DateTime)

    '''
    Establishes a collection of Legoset objects on Watch
    '''
    legoset = db.relationship('Legoset')

    def __init__(self, user_id, legoset):
        self.user_id = user_id
        self.legoset.append(legoset)
        self.added = dt.utcnow()

    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'lego_set': self.legoset,
            'added': self.added
        }


class User(BaseModel):
    '''
    Model for User
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    added = db.Column(db.DateTime)
    '''
    Establishes a collection of Watch objects on User
    and a .watches_user attribute on Watch
    '''
    watches = db.relationship('Watch', back_populates='user', lazy='dynamic')

    def __init__(self, email):
        self.email = email
        self.added = dt.utcnow()

    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'added': self.added
        }


class StockLevel(BaseModel):
    '''
    Model storing a stock level datapoint
    '''
    __tablename__ = 'stocklevel'
    id = db.Column(db.Integer, primary_key=True)
    legoset_id = db.Column(db.Integer, db.ForeignKey('legoset.id'))
    datetime = db.Column(db.DateTime)
    stock_level = db.Column(db.Integer)

    def __init__(self, lego_set, stock_level):
        self.lego_set = lego_set
        self.stock_level = stock_level
        self.datetime = dt.utcnow()


    def to_dict(self):
        return {
            'id': self.id,
            'lego_set': self.lego_set,
            'stock_level': self.stock_level,
            'datetime': self.datetime
        }

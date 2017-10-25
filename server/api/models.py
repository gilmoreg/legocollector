"""
  Model definitions
"""
from datetime import datetime as dt

from api.database import db

'''
Establish many-to-many relationship between Users and Legosets called 'watches'
'''
watch_table = db.Table('user_legoset_association', db.metadata,
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('legoset_id', db.Integer, db.ForeignKey('legoset.id')))


# noinspection PyCompatibility
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


class StockLevel(BaseModel):
    """
    Model storing a stock level datapoint
    """
    __tablename__ = 'stocklevel'
    id = db.Column(db.Integer, primary_key=True)
    legoset_id = db.Column(db.Integer, db.ForeignKey('legoset.id'))
    datetime = db.Column(db.DateTime, default=dt.utcnow)
    stock_level = db.Column(db.Integer)

    def __init__(self, stock_level, *args):
        super().__init__(*args)
        self.stock_level = stock_level

    def to_dict(self):
        return {
            'id': self.id,
            'stock_level': self.stock_level,
            'datetime': self.datetime
        }


class LegoSet(BaseModel):
    """
    Model for watched Lego set
    """
    __tablename__ = 'legoset'
    # Equal to the official lego Set Number
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))
    url = db.Column(db.String(255))
    added = db.Column(db.DateTime, default=dt.utcnow)

    stock_levels = db.relationship(StockLevel, uselist=True, order_by="StockLevel.datetime")

    def __init__(self, legoset, *args):
        super().__init__(*args)
        self.id = legoset['id']
        self.title = legoset['title']
        self.image = legoset['image']
        self.url = legoset['url']

    def cull_stock(self):
        """ Limit stock_levels to 30 datapoints """
        if len(self.stock_levels) > 30:
            # Stock levels already sorted by date
            # Keep only the most recent 29
            self.stock_levels[:] = self.stock_levels[-30:]
            self.save()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'url': self.url,
            'added': self.added,
            'stock_levels': list(map(lambda s: s.to_dict(), self.stock_levels))
        }


class User(BaseModel):
    """
    Model for User
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    added = db.Column(db.DateTime, default=dt.utcnow)

    watches = db.relationship(LegoSet, secondary=watch_table)

    def __init__(self, email, *args):
        super().__init__(*args)
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'added': self.added,
            'watches': list(map(lambda w: w.to_dict(), self.watches))
        }

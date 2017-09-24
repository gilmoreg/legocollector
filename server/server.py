'''
    Python/Flask REST API for Legocollector
'''
from datetime import datetime as dt
from flask import Flask, jsonify, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import Watch, User, StockLevel

app = Flask(__name__)
app.config.from_envvar('SETTINGS')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def connect_db():
    ''' Connect to Postgres database '''
    if not hasattr(g, 'db'):
        g.db = db
    return g.db

@app.route('/watches', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    return jsonify({'result': 'all watches'})

@app.route('/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    return jsonify({'result': 'new_watch'})


class Watch(db.Model):
  '''
  Model for Watch
  '''
  __tablename__ = 'watches'
  set_id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.Integer)
  added = db.Column(db.Date)

  def __init__(self, set_id, user):
    self.set_id = set_id
    self.user = user
    self.added = dt.utcnow()

  def __repr__(self):
    return jsonify({'set_id': self.set_id, 'user': self.user, 'added': self.added})

class User(db.Model):
  '''
  Model for User
  '''
  __tablename__ = 'users'
  user_id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String)

  def __init__(self, email):
    self.email = email
  
  def __repr__(self):
    return jsonify({'id': self.user_id, 'email': self.email})

class StockLevel(db.Model):
  '''
  Model storing a stock level datapoint
  '''
  __tablename__ = 'stocklevels'
  stocklevel_id = db.Column(db.Integer, primary_key=True)
  set_id = db.Column(db.Integer)
  time = db.Column(db.Date)
  stock_level = db.Column(db.Integer)

  def __init__(self, set_id):
    self.set_id = set_id
    self.time = dt.utcnow()
  
  def __repr__(self):
    return jsonify({'id': self.stocklevel_id, 'set_id': self.set_id, 'stock_level': self.stock_level})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

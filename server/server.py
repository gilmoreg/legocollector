'''
    Python/Flask REST API for Legocollector
'''
from datetime import datetime as dt
from flask import Flask, jsonify, request, g
from flask_pymongo import PyMongo

APP = Flask(__name__)
APP.config.from_envvar('SETTINGS')
MONGO = PyMongo(APP)

def connect_db():
    ''' Connect to MongoDB '''
    if not hasattr(g, 'mongo'):
        g.mongo = MONGO
    return g.mongo.db

@APP.route('/', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    connect_db()
    watches = g.mongo.db.watches
    output = []

    for q in watches.find():
        output.append({'set_id': q['set_id']})

    return jsonify({'result': output})

@APP.route('/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    watches = g.mongo.db.watches
    set_id = request.json['set_id']
    added = dt.utcnow()

    new_id = watches.insert({'set_id': set_id, 'added': added})
    new_watch = watches.find_one({'_id': str(new_id)})
    return jsonify({'result': new_watch})

if __name__ == '__main__':
    APP.run(host='0.0.0.0')

'''
    Python/Flask REST API for Legocollector
'''
from flask import Flask #, jsonify, request
from flask_pymongo import PyMongo

APP = Flask(__name__)
APP.config.from_envvar('SETTINGS')
MONGO = PyMongo(APP)


@APP.route('/', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    watches = MONGO.db.watches
    output = []

    for q in watches.find():
        output.append({'name': q['name']})

    return jsonify({'result': output})

if __name__ == '__main__':
    APP.run(debug=APP.config['DEBUG'])

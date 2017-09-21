from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo

APP = Flask(__name__)

APP.config['MONGO_DBNAME'] = 'legotools'
APP.config['MONGO_URI'] = 'mongodb://<dbuser>:<dbpassword>@ds141514.mlab.com:41514/legotools'

MONGO = PyMongo(APP)

@APP.route('/')
def get_all_watches():
    watches = MONGO.db.watches
    output = []
    for q in watches.find():
        output.append({'name': q['name']})

    return jsonify({'result': output})

if __name__ == '__main__':
    APP.run(debug=True)

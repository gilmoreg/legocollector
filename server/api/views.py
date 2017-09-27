'''
    Python/Flask REST API for Legocollector
'''
from flask import request, jsonify
from api import app
import api.controller as controller


@app.route('/watches', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    return controller.get_all_watches()


@app.route('/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    # TOOD rip stuff off request
    return controller.add_watch()


@app.route('/set/add/<id>', methods=['POST'])
def add_legoset(id):
    return controller.add_legoset(id)


@app.route('/login', methods=['POST'])
def login():
    '''
        Accepts a POST body with an access_token from Amazon
        Passes this along to the login controller which handles
        database and authentication operations

        Note: Flask request.form requires a content-type header of form-data
        or x-www-form-urlencoded, cannot be raw
    '''
    data = request.get_json(force=True)
    try:
        return controller.login(data['access_token'])
    except KeyError as e:
        # TODO proper restful error response
        return jsonify(
            {'error': 'Must supply an access_token and a content-type'}
        )

'''
    /api/views/login.py
    Views for authentication
'''
from flask import Blueprint, request, jsonify
from api.controllers import auth_controller


blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=['POST'])
def login():
    '''
        Accepts a POST body with an access_token from Amazon
        Passes this along to the login controller which handles
        database and authentication operations
    '''
    data = request.get_json(force=True)
    try:
        return auth_controller.login(data['access_token'])
    except KeyError as e:
        # TODO proper restful error response
        return jsonify(
            {'error': 'Must supply an access_token and a content-type'}
        )

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
        profile = auth_controller.login(data['access_token'])
        return jsonify({'result': profile})
    except Exception as e:
        return e

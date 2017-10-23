"""
    /api/views/login.py
    Views for authentication
"""
from flask import Blueprint, request, jsonify
from api.controllers.auth import login
from api.errors import FlaskError, exception_json_response

blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=['POST'])
def login_route():
    """
    Accepts a POST body with an access_token from Amazon
    If the token is good, either authenticates or creates a new user from it
    """
    data = request.get_json(force=True)
    try:
        result = login(data['access_token'])
        return jsonify({'result': result})
    except FlaskError as e:
        print('/login view error', e)
        return e.json_response()
    except Exception as e:
        print('/login view error', e)
        return exception_json_response(e)

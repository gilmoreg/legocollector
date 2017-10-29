"""
    /api/views/legoset.py
    Views for /legoset
"""
import re

from flask import Blueprint, jsonify, request
from api.controllers.auth import authenticate, verify_admin
from api.controllers.legoset import search, update_stock_levels
from api.errors import FlaskError, exception_json_response

blueprint = Blueprint('legoset', __name__)


@blueprint.route('/legoset/search/<id>', methods=['GET'])
def find_legoset_view(id):
    """
    Return json repr of LegoSet
    :param id: LEGO set id
    :rtype: json
    :raises: ValueError
    :raises: FlaskError
    """
    try:
        # ID must be an integer between 5 and 7 digits
        test = re.match(r'^\d{5,7}$', id)
        if not test:
            raise ValueError
        token = request.args.get('token')
        authenticate(token)
        legoset = search(int(id))
        return jsonify({'result': legoset})
    except ValueError:
        error = FlaskError('Please supply a valid query (a 5 to 7 digit integer)', status_code=400)
        return error.json_response()
    except FlaskError as e:
        return e.json_response()


@blueprint.route('/legoset/update', methods=['POST'])
def update():
    """
    This endpoint is called by an AWS Lambda running every 6 hours
    With 30 datapoints this ensures about a week's worth of stock data
    :returns: json result - 'success' or 'unauthorized'
    :rtype: json
    """
    data = request.get_json(force=True)
    if verify_admin(data['token']):
        update_stock_levels()
        return jsonify({'result': 'success'})
    return jsonify({'result': 'unauthorized'})

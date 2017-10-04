'''
    /api/views/watches.py
    Views for /watches
'''
from flask import Blueprint, request, jsonify
from api.controllers import watch_controller


blueprint = Blueprint('watches', __name__)


@blueprint.route('/watches', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    return watch_controller.get_all_watches()


@blueprint.route('/watches/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    data = request.get_json(force=True)
    try:
        return watch_controller.add_watch(data['token'], data['id'])
    except KeyError as e:
        # TODO proper restful error response
        return jsonify(
            {'error': 'Must supply an access_token and a set ID'}
        )


'''
    /api/views/watches.py
    Views for /watches
'''
from flask import Blueprint, request, jsonify
from api.controllers.watch_controller import WatchController
from api.errors import FlaskError

blueprint = Blueprint('watches', __name__)

@blueprint.route('/watches', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    try:
        watches = WatchController.get_all_watches()
        return jsonify({'result': watches})
    except Exception as e:
        return e


@blueprint.route('/watches/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    data = request.get_json(force=True)
    try:
        watch = watch_controller.add_watch(data['token'], data['id'])
        return jsonify({'result': watch})
    except:
        raise FlaskError('Must supply an access_token and a set ID', status_code=400)

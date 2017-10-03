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
    return watch_controller.add_watch(data)


"""
    /api/views/watches.py
    Views for /watches
"""
from flask import Blueprint, request, jsonify, current_app
from api.controllers.watch_controller import WatchController
from api.errors import FlaskError, exception_json_response


blueprint = Blueprint('watches', __name__)
watch_controller = WatchController()


@blueprint.route('/watches', methods=['GET'])
def get_users_watches():
    """ Return all watched sets for a user """
    try:
        token = request.args.get('token')
        watches = watch_controller.get_users_watches(token)
        return jsonify({'result': watches})
    except Exception as e:
        return exception_json_response(e)


@blueprint.route('/watches/<id>', methods=['GET'])
def get_watch(id):
    """ Return specific watch """
    try:
        watch_id = id or request.args.get('id')
        token = request.args.get('token')
        watch = watch_controller.get_watch(id, token)
        return jsonify({'result': watch})
    except Exception as e:
        return exception_json_response(e)


@blueprint.route('/watches/add', methods=['POST'])
def add_watch():
    """ Add a watched set to the database, return JSON """
    data = request.get_json(force=True)
    try:
        watch = watch_controller.add_watch(data['token'], data['id'])
        return jsonify({'result': watch})
    except KeyError:
        error = FlaskError('Must supply a token and a set ID', status_code=400)
        return error.json_response()
    except Exception as e:
        return exception_json_response(e)  


@blueprint.route('/watches/delete/<id>', methods=['POST'])
def delete_watch(id):
    """ Delete specified watch """
    watch_id = id or request.args.get('id')
    data = request.get_json(force=True)
    try:
        watch_controller.delete_watch(data['token'], watch_id)
        return jsonify({'result': 'Watch ' + watch_id + ' deleted'})
    except KeyError:
        error = FlaskError('Must supply a token and a set ID', status_code=400)
        return error.json_response()
    except Exception as e:
        return exception_json_response(e)

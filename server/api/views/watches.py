"""
    /api/views/watches.py
    Views for /watches
"""
from flask import Blueprint, request, jsonify, current_app
from api.controllers.auth import get_user
from api.controllers.legoset import get_or_create_legoset
from api.controllers.watch import add_watch, get_users_watches, get_watch, delete_watch
from api.errors import FlaskError, exception_json_response

blueprint = Blueprint('watches', __name__)


@blueprint.route('/watches', methods=['GET'])
def get_users_watches_route():
    """ Return all watched sets for a user """
    try:
        token = request.args.get('token')
        watches = get_users_watches(token)
        return jsonify({'result': watches})
    except Exception as e:
        return exception_json_response(e)


@blueprint.route('/watches/<w_id>', methods=['GET'])
def get_watch_route(w_id):
    """ Return specific watch """
    try:
        watch_id = w_id or request.args.get('w_id')
        token = request.args.get('token')
        watch = get_watch(watch_id, token)
        return jsonify({'result': watch})
    except Exception as e:
        return exception_json_response(e)


@blueprint.route('/watches/add', methods=['POST'])
def add_watch_route():
    """ Add a watched set to the database, return JSON """
    data = request.get_json(force=True)
    try:
        set_id = data['id']
        token = data['token']
        # Perform this check early to ensure authentication
        user = get_user(token)
        legoset = get_or_create_legoset(set_id)
        if legoset is None:
            raise FlaskError('Could not create legoset ' + set_id, status_code=400)
        watch = add_watch(user, legoset)
        return jsonify({'result': watch})
    except KeyError:
        error = FlaskError('Must supply a token and a set ID', status_code=400)
        return error.json_response()
    except FlaskError as e:
        return e.json_response()
    except Exception as e:
        return exception_json_response(e)  


@blueprint.route('/watches/delete/<w_id>', methods=['POST'])
def delete_watch_route(w_id):
    """ Delete specified watch """
    watch_id = w_id or request.args.get('w_id')
    data = request.get_json(force=True)
    try:
        delete_watch(data['token'], watch_id)
        return jsonify({'result': 'Watch ' + watch_id + ' deleted'})
    except KeyError:
        error = FlaskError('Must supply a token and a set ID', status_code=400)
        return error.json_response()
    except Exception as e:
        return exception_json_response(e)

'''
    /api/views/legoset.py
    Views for /legoset
'''
from flask import Blueprint, jsonify, request, current_app
from api.controllers.legoset_controller import LegoSetController
from api.errors import FlaskError, exception_json_response

blueprint = Blueprint('legoset', __name__)
legoset_controller = LegoSetController()

@blueprint.route('/legoset/add/<id>', methods=['POST'])
def add_legoset_view(id):
    try:
        set_id = id or request.args.get('id')
        data = request.get_json(force=True)
        legoset = legoset_controller.add_legoset(set_id, data['token'])
        return jsonify({'result': legoset})
    except KeyError:
        error = FlaskError('Must supply a set_id and a valid token', status_code=400)
        return error.json_response()
    except FlaskError as e:
        return e.json_response()
    except Exception as e:
        return exception_json_response(e)

@blueprint.route('/legoset/search/<id>', methods=['GET'])
def find_legoset_view(id):
    try:
        set_id = id or request.args.get('id')
        token = request.args.get('token')
        legoset = legoset_controller.search(set_id, token)
        return jsonify({'result': legoset})
    except KeyError:
        error = FlaskError('Must supply a set_id and a valid token', status_code=400)
        return error.json_response()
    except FlaskError as e:
        return e.json_response()
    except Exception as e:
        return exception_json_response(e)

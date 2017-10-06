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
        legoset = legoset_controller.add_legoset(set_id)
        return jsonify({'result': legoset.to_dict()})
    except FlaskError as e:
        return e.json_response()
    except Exception as e:
        return exception_json_response(e)

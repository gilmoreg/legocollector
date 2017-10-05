'''
    /api/views/legoset.py
    Views for /legoset
'''
from flask import Blueprint, jsonify, request
from api.controllers.legoset_controller import LegoSetController

blueprint = Blueprint('legoset', __name__)
legoset_controller = LegoSetController()

@blueprint.route('/legoset/add/<id>', methods=['POST'])
def add_legoset_view(id):
    try:
        set_id = id or request.args.get('id')
        legoset = legoset_controller.add_legoset(set_id)
        return jsonify({'result': legoset.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)})

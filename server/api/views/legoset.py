'''
    /api/views/legoset.py
    Views for /legoset
'''
from flask import Blueprint, jsonify
from api.controllers.legoset_controller import LegoSetController

blueprint = Blueprint('legoset', __name__)


@blueprint.route('/legoset/add/<id>', methods=['POST'])
def add_legoset(id):
    try:
        legoset = LegoSetController.add_legoset(id)
        return jsonify({'result': legoset})
    except Exception as e:
        return e

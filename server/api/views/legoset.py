'''
    /api/views/legoset.py
    Views for /legoset
'''
from flask import Blueprint
from api.controllers import legoset_controller


blueprint = Blueprint('legoset', __name__)


@blueprint.route('/legoset/add/<id>', methods=['POST'])
def add_legoset(id):
    return legoset_controller.add_legoset(id)

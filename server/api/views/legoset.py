'''
    /api/views/legoset.py
    Views for /legoset
'''
from flask import Blueprint, jsonify, request, current_app
from api.controllers.legoset_controller import LegoSetController
from api.errors import FlaskError

blueprint = Blueprint('legoset', __name__)
legoset_controller = LegoSetController()

@blueprint.route('/legoset/add/<id>', methods=['POST'])
def add_legoset_view(id):
    try:
        set_id = id or request.args.get('id')
        legoset = legoset_controller.add_legoset(set_id)
        return jsonify({'result': legoset.to_dict()})
    except FlaskError as e:
        error = e.to_dict()
        return jsonify({'error': error['message']}), error['status_code']
    except Exception as e:
        if current_app.config['ENV'] == 'prod':
            return jsonify({'error': 'Something went wrong'}), 500
        return jsonify({'error': str(e)}), 500

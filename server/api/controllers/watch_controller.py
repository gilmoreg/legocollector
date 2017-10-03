'''
    /api/controllers/watch_controller.py
    Controller for /watches routes
'''
from flask import jsonify
from api.models import LegoSet, Watch


def get_all_watches():
    ''' Return all Watches '''
    watches = Watch.query.all()
    return jsonify({'result': watches})


def add_watch(token, set_id):
    '''
    POST /watch/add

    Add a new watch to the database
    If the set doesn't exist yet, add it first
    '''
    user = authenticate(token)
    if user is not None:
        lego_set = LegoSet.query.filter_by(id=set_id).first()
        if lego_set is None:
            ''' create new lego set '''
            lego_set = add_legoset(set_id)
        new_watch = Watch(user, lego_set)
        return jsonify({'result': new_watch})
    return jsonify({'error': 'Could not authenticate user'})


# def remove_watch(user, id)

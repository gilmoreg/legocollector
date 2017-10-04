'''
    /api/controllers/watch_controller.py
    Controller for /watches routes
'''
from flask import jsonify
import json
from api.models import LegoSet, Watch
from api.controllers.auth_controller import authenticate
from api.controllers.legoset_controller import add_legoset


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
            '''
                Given how interdependent these controller
                functions are, should probably only
                return jsonify in the views,
                which are pretty empty now
                have to decide how to return errors
                Could raise exceptions here,
                have views do the try/catch
            '''
            new_lego_set = add_legoset(set_id)
            lego_set = json.loads(new_lego_set.data.decode('utf8'))
        new_watch = Watch(user, lego_set.id)
        new_watch.save()
        return jsonify({'result': new_watch})
    return jsonify({'error': 'Could not authenticate user'})


# def remove_watch(user, id)

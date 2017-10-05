'''
    /api/controllers/watch_controller.py
    Controller for /watches routes
'''
import json
from api.models import LegoSet, Watch
from api.controllers.auth_controller import AuthController
from api.controllers.legoset_controller import LegoSetController
from api.errors import FlaskError


class WatchController(object):
    ''' Controller for watches '''
    def get_all_watches():
        ''' Return all Watches '''
        watches = Watch.query.all()
        return watches


    def add_watch(token, set_id):
        '''
        POST /watch/add

        Add a new watch to the database
        If the set doesn't exist yet, add it first
        '''
        user = AuthController.authenticate(token)
        if user is not None:
            lego_set = LegoSet.query.filter_by(id=set_id).first()
            if lego_set is None:
                ''' create new lego set '''
                new_lego_set = LegoSetController.add_legoset(set_id)
            new_watch = Watch(user, new_lego_set.id)
            new_watch.save()
            return new_watch
        raise FlaskError('Could not authenticate user', status_code=401)


# def remove_watch(user, id)
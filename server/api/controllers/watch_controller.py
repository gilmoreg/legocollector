'''
    /api/controllers/watch_controller.py
    Controller for /watches routes
'''
import json
from api.models import LegoSet, Watch, User
from api.controllers.auth_controller import AuthController
from api.controllers.legoset_controller import LegoSetController
from api.errors import FlaskError


class WatchController(object):
    ''' Controller for watches '''
    def get_users_watches(self, token):
        ''' Return all of a user's Watches '''
        # Verify valid user (will raise an exception if it fails)
        user_id = AuthController.authenticate(token)
        watches = Watch.query.filter_by(user=user_id)
        return list(map(lambda w: w.to_dict(), watches))


    def get_watch(self, watch_id, token):
        ''' Get specificed watch '''
        # Verify valid user (will raise an exception if it fails)
        user_id = AuthController.authenticate(token)
        # Query db for watch
        watch = Watch.query.filter_by(id=watch_id, user=user_id).first()
        if watch is not None:
            return watch.to_dict()
        raise FlaskError('Watch not found', status_code=400)
        

    def add_watch(self, token, set_id):
        '''
        POST /watch/add

        Add a new watch to the database
        If the set doesn't exist yet, add it first
        '''
        # Verify valid user (will raise an exception if it fails)
        user = AuthController.authenticate(token)
        # Check if set exists; if not, create it
        lego_set = LegoSet.query.filter_by(id=set_id).first()
        if lego_set is None:
            ''' create new lego set '''
            legoset_controller = LegoSetController()
            lego_set = legoset_controller.create_legoset_record(set_id=set_id)
        else:
            lego_set = lego_set.to_dict()
        new_watch = Watch(user, lego_set['id'])
        new_watch.save()
        return new_watch.to_dict()
        

# def remove_watch(user, id)

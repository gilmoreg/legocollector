"""
    /api/controllers/watch_controller.py
    Controller for /watches routes
"""
from api.controllers.auth_controller import AuthController
from api.controllers.legoset_controller import LegoSetController
from api.models import LegoSet
from api.errors import FlaskError


class WatchController(object):
    """ Controller for watches """
    @staticmethod
    def get_users_watches(token):
        """ Return all of a user's Watches """
        user = AuthController.get_user(token)
        return list(map(lambda w: w.to_dict(), user.watches))

    @staticmethod
    def get_watch(set_id, token):
        """ Return a specific watch """
        user = AuthController.get_user(token)
        for watch in user.watches:
            if watch.id == int(set_id):
                return watch.to_dict()

    @staticmethod
    def add_watch(token, set_id):
        """
        POST /watch/add

        Add a new watch to the database
        If the set doesn't exist yet, add it first
        """
        user = AuthController.get_user(token)
        # Check if set exists; if not, create it
        lego_set = LegoSet.query.filter_by(id=set_id).first()
        if lego_set is None:
            ''' create new lego set '''
            legoset_controller = LegoSetController()
            lego_set = legoset_controller.create_legoset_record(set_id=set_id)
        user.watches.append(lego_set)
        user.save()
        # Return the newly created set
        return lego_set.to_dict()

    @staticmethod
    def delete_watch(token, set_id):
        """ Cease watching LegoSet set_id for user """
        user = AuthController.get_user(token)
        for watch in user.watches:
            if watch.id == int(set_id):
                user.watches.remove(watch)
                user.save()
                return set_id
        raise FlaskError('Watch not found', status_code=400)

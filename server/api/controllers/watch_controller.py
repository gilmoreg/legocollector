"""
    /api/controllers/watch_controller.py
    Controller for /watches routes
"""
from api.controllers.auth_controller import AuthController
from api.controllers.legoset_controller import LegoSetController
from api.models import LegoSet


class WatchController(object):
    """ Controller for watches """

    def get_users_watches(self, token):
        """ Return all of a user's Watches """
        user = AuthController.get_user(token)
        return list(map(lambda w: w.to_dict(), user.watches))

    def add_watch(self, token, set_id):
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

# def remove_watch(user, id)

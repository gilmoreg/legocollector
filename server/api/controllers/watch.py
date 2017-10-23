"""
    /api/controllers/watch_controller.py
    Controller for /watches routes
"""
from api.controllers.auth import get_user
from api.errors import FlaskError


def get_users_watches(token):
    """ Return all of a user's Watches """
    user = get_user(token)
    return list(map(lambda w: w.to_dict(), user.watches))


def get_watch(set_id, token):
    """ Return a specific watch """
    user = get_user(token)
    for watch in user.watches:
        if watch.id == int(set_id):
            return watch.to_dict()


def add_watch(user, legoset):
    """
    POST /watch/add

    Add a new watch to the database
    If the set doesn't exist yet, add it first
    """
    user.watches.append(legoset)
    user.save()
    return legoset.to_dict()


def delete_watch(token, set_id):
    """ Cease watching LegoSet set_id for user """
    user = get_user(token)
    for watch in user.watches:
        if watch.id == int(set_id):
            user.watches.remove(watch)
            user.save()
            return set_id
    raise FlaskError('Watch not found', status_code=400)

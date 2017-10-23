"""
    /api/controllers/watch_controller.py
    Controller for /watches routes
"""
from api.errors import FlaskError


def get_users_watches(user):
    """ Return all of a user's Watches """
    return list(map(lambda w: w.to_dict(), user.watches))


def get_watch(set_id, user):
    """ Return a specific watch """
    for watch in user.watches:
        if watch.id == int(set_id):
            return watch.to_dict()


def add_watch(legoset, user):
    """
    POST /watch/add

    Add a new watch to the database
    If the set doesn't exist yet, add it first
    """
    if legoset in user.watches:
        raise FlaskError('Watch already exists for user', status_code=400)
    user.watches.append(legoset)
    user.save()
    return legoset.to_dict()


def delete_watch(set_id, user):
    """ Cease watching LegoSet set_id for user """
    for watch in user.watches:
        if watch.id == int(set_id):
            user.watches.remove(watch)
            user.save()
            return set_id
    raise FlaskError('Watch not found', status_code=400)

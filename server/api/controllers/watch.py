"""
    /api/controllers/watch_controller.py
    Controller for /watches routes
"""
from api.errors import FlaskError


def get_users_watches(user):
    """
    Return all of a user's Watches
    :param user: User object
    :returns: list of Watch objects
    :rtype: list
    """
    return list(map(lambda w: w.to_dict(), user.watches))


def get_watch(set_id, user):
    """
    Return a specific watch
    :param set_id: LEGO set id
    :param user: User object
    :returns: dict repr of Watch object
    :rtype: dict
    """
    for watch in user.watches:
        if watch.id == int(set_id):
            return watch.to_dict()


def add_watch(legoset, user):
    """
    POST /watch/add
    Add a new watch to the database
    :param legoset: LegoSet object
    :param user: User object
    :returns: dict repr of LegoSet object
    :rtype: dict
    """
    if legoset in user.watches:
        print('watch already exists for user')
        raise FlaskError('Watch already exists for user', status_code=400)
    user.watches.append(legoset)
    user.save()
    return legoset.to_dict()


def delete_watch(set_id, user):
    """
    Cease watching LegoSet set_id for user
    :param set_id: LEGO set id
    :param user: User object
    :returns: LEGO set id
    :rtype: string
    """
    for watch in user.watches:
        if watch.id == int(set_id):
            user.watches.remove(watch)
            user.save()
            return set_id
    raise FlaskError('Watch not found', status_code=400)

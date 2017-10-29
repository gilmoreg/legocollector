""" Factories for tests """
from api.controllers.auth import create_jwt
from api.models import User, LegoSet


def create_user(email):
    """
    Add a User to the database and create a valid JWT for it
    :param email: email address
    :return: dict of JWT (token), email, User object
    :rtype: dict
    """
    user = User(email).save()
    token = create_jwt(user.id)
    return {'token': token, 'email': email, 'user': user}


def create_legoset(id):
    """
    Create a LegoSet in the database
    :param id: LEGO set id
    :return: LegoSet object
    """
    legoset = LegoSet({
        'id': id,
        'title': 'Test Lego Set',
        'image': 'test',
        'url': 'test'
    }).save()
    return legoset


def create_watch(legoset, user):
    """
    Create a Watch object in the database
    :param legoset: LegoSet object
    :param user: User object
    :return: Watch object
    """
    user.watches.append(legoset)
    user.save()
    return user

""" Factories for tests """
from api.controllers.auth import create_jwt
from api.models import User, LegoSet


def create_user(email):
    user = User(email).save()
    token = create_jwt(user.id)
    return {'token': token, 'email': email, 'user': user}


def create_legoset(id):
    legoset = LegoSet({
        'id': id,
        'title': 'Test Lego Set',
        'image': 'test',
        'url': 'test'
    }).save()
    return legoset


def create_watch(legoset, user):
    user.watches.append(legoset)
    user.save()
    return user

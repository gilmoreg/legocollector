''' Factories for tests '''
from api.models import User, LegoSet, StockLevel
from api.controllers.auth_controller import AuthController


def create_user(email):
    user = User(email).save()
    token = AuthController.create_jwt(user.id)
    return {'token': token, 'email': email, 'user': user}

def create_legoset(id):
    legoset = LegoSet({
        'id': id,
        'title': 'Test Lego Set',
        'image': 'test',
        'url': 'test'
    }).save()
    return legoset


def create_watch(user, legoset):
    user.watches.append(legoset)
    user.save()
    return user

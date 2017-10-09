''' Factories for tests '''
from api.models import User, LegoSet, Watch, StockLevel
from api.controllers.auth_controller import AuthController


def create_user(email):
    user = User(email).save()
    token = AuthController.create_jwt(user.id)
    return {'token': token, 'email': email, 'id': user.id}

def create_legoset(id):
    legoset = LegoSet({
        'id': id,
        'title': 'Test Lego Set',
        'image': 'test',
        'url': 'test'
    }).save()
    return legoset.to_dict()

def create_watch(user_id, legoset_id):
    watch = Watch(user_id, legoset_id).save()
    return watch.to_dict()

"""
/server/api/auth.py
Authentication service
"""
import jwt
from os import environ
from api.models import User
from api.errors import FlaskError


def create_jwt(user_id):
    """ Create JSON Web Token and decode to string """
    token = jwt.encode(
        {'user': user_id},
        environ['JWT_SECRET'],
        algorithm='HS256')
    return token.decode('utf-8')


def authenticate(token):
    """ Decode JWT and extract user id """
    try:
        decoded = jwt.decode(token, environ['JWT_SECRET'], algorithms=['HS256'])
        return decoded['user']
    except:
        ''' If token is invalid raise an error '''
        raise FlaskError('Could not authenticate user', status_code=401)


def get_user(token):
    """ Get a User object from a token """
    user_id = authenticate(token)
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return user
    raise FlaskError('User not found', status_code=401)


def verify_admin(token):
    """ Verify this token carries administrator privileges """
    try:
        user = authenticate(token)
        if user == environ['ADMIN']:
            return True
        return False
    except Exception as e:
        print('verify_admin exception', e)
        return False
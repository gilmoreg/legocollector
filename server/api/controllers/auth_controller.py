'''
    /api/controllers/auth_controller.py
    Controller for authentication
'''
import jwt
import requests
from os import environ
from api.models import User
from api.errors import FlaskError


class AuthController(object):
    ''' Controller for authentication '''
    def create_jwt(user_id):
        ''' Create JSON Web Token and decode to string '''
        token = jwt.encode(
            {'user': user_id},
            environ['JWT_SECRET'],
            algorithm='HS256')
        return token.decode('utf-8')


    def authenticate(token):
        ''' Decode JWT and extract user id '''
        try:
            decoded = jwt.decode(token, environ['JWT_SECRET'], algorithms=['HS256'])
            return decoded['user']
        except:
            ''' If token is invalid raise an error '''
            raise FlaskError('Could not authenticate user', status_code=401)


    def login(amazon_token):
        '''
        Performs the following:
        1. Asks Amazon about this access token
        2. Gets an email address
        3. Sees if that email exists in the db
        If not, creates that user
        4. Signs the user id into a JWT
        5. Returns token and the email (for display purposes) to the user
        for future requests
        The client side can then stash the JWT in localStorage
        '''
        profile = requests.get(
            'https://api.amazon.com/user/profile?access_token={}'
            .format(amazon_token)).json()
        if 'email' in profile:
            user = User.query.filter_by(email=profile['email']).first()
            if user is not None:
                token = create_jwt(user.id)
                return {'token': token, 'email': profile['email']}
            else:
                new_user = User(profile['email']).save()
                token = create_jwt(new_user.id)
                return {'token': token, 'email': profile['email']}
        raise FlaskError('Could not authenticate user', status_code=401)

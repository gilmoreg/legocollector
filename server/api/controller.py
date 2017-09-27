'''
  Controller
'''
from api.models import Watch, LegoSet, User
from flask import jsonify
from os import environ
import requests
import bottlenose
from bs4 import BeautifulSoup
import jwt


amazon = bottlenose.Amazon(
    environ['AWS_ACCESS_KEY_ID'],
    environ['AWS_SECRET_ACCESS_KEY'],
    environ['AWS_ASSOCIATE_TAG'],
    Parser=lambda text: BeautifulSoup(text, 'lxml'))


def create_jwt(user_id):
    ''' Create JSON Web Token and decode to string '''
    token = jwt.encode(
        {'user': user_id},
        environ['JWT_SECRET'],
        algorithm='HS256')
    return token.decode('utf-8')


def get_all_watches():
    ''' Return all Watches '''
    watches = Watch.query.all()
    return jsonify({'result': watches})


def add_legoset(set_id):
    ''' Fetch data about a legoset from Amazon and add to the database '''
    id = str(set_id)
    response = amazon.ItemSearch(Keywords="Lego {}".format(id),
                                 Title=id,
                                 SearchIndex="Toys",
                                 # MerchantId="Amazon",
                                 ResponseGroup="Images,OfferSummary,Small")
    item = response.find('item')
    if item is not None:
        new_legoset_options = {
          'id': id,
          'url': item.find('detailpageurl').get_text(),
          'title': item.find('itemattributes').find('title').get_text(),
          'image': item.find('mediumimage').find('url').get_text()
        }
        new_legoset = LegoSet(new_legoset_options)
        try:
            new_legoset.save()
            return jsonify({'result': new_legoset})
        except:
            return jsonify({'error': 'Unable to save new set to database'})

    return jsonify({'error': 'Could not find set {} on Amazon'.format(id)})


# def remove_legoset(id)


def add_watch(user, set_id):
    '''
    Add a new watch to the database
    If the set doesn't exist yet, add it first
    '''
    lego_set = LegoSet.query.filter_by(id=set_id).first()
    if lego_set is None:
        ''' create new lego set '''
        new_lego_set = add_legoset(id)

    return 'new_watch'


# def remove_watch(user, id)


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
            token = create_jwt(new_user.id)
            return jsonify({'token': token})
        else:
            new_user = User(profile['email']).save()
            token = create_jwt(new_user.id)
            return jsonify({'token': token})
    return jsonify({'error': 'Could not authenticate user'})

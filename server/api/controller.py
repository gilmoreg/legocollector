'''
  Controller
'''
from api.models import Watch, LegoSet
from flask import jsonify
from os import environ
import bottlenose
from bs4 import BeautifulSoup

amazon = bottlenose.Amazon(
    environ['AWS_ACCESS_KEY_ID'],
    environ['AWS_SECRET_ACCESS_KEY'],
    environ['AWS_ASSOCIATE_TAG'],
    Parser=lambda text: BeautifulSoup(text, 'lxml'))


def get_all_watches():
    ''' Return all Watches '''
    watches = Watch.query.all()
    return jsonify({'result': watches})


def add_legoset(id):
    ''' Fetch data about a legoset from Amazon and add to the database '''
    response = amazon.ItemSearch(Keywords="Lego {}".format(str(id)),
                                 Title=str(id),
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
        new_legoset.save()
        return new_legoset

    return None


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

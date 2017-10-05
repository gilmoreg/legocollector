'''
    /api/controllers/legoset_controller.py
    Controller for legosets
'''
from api.models import LegoSet
from api.errors import FlaskError
from os import environ
import bottlenose
from bs4 import BeautifulSoup


class LegoSetController(object):
    '''
        Controller for legosets
    '''
    amazon = None

    def __init__(self, amazon=None):
        ''' Create bottlenose instance if not injected for testing '''
        if amazon is not None:
            self.amazon = amazon
        else:
            self.amazon = bottlenose.Amazon(
                environ['AWS_ACCESS_KEY_ID'],
                environ['AWS_SECRET_ACCESS_KEY'],
                environ['AWS_ASSOCIATE_TAG'],
                Parser=lambda text: BeautifulSoup(text, 'lxml'))


    def add_legoset(self, set_id):
        ''' Fetch data about a legoset from Amazon and add to the database '''
        id = str(set_id)
        response = self.amazon.ItemSearch(Keywords="Lego {}".format(id),
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
            set_exists = LegoSet.query.filter_by(id=id).first()
            if set_exists:
                return set_exists
            new_legoset = LegoSet(new_legoset_options)
            try:
                new_legoset.save()
                return new_legoset
            except:
                raise FlaskError('Unable to save new set to database', status_code=500)
        raise FlaskError('Could not find set {} on Amazon'.format(id), status_code=400)


    #  def remove_legoset(self, id)

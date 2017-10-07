'''
    /api/controllers/legoset_controller.py
    Controller for legosets
'''
from flask import g, current_app
from api.amazon import Amazon
from api.models import LegoSet
from api.errors import FlaskError


class LegoSetController(object):
    '''
        Controller for legosets
    '''
    def add_legoset(self, set_id):
        ''' Fetch data about a legoset from Amazon and add to the database '''
        id = str(set_id)
        # Check if set exists already; if so raise an error but also 200 OK response
        set_exists = LegoSet.query.filter_by(id=id).first()
        if set_exists:
            raise FlaskError('Set {} already exists in the database'.format(id), status_code=200)
        # Query Amazon API for info about the set
        amazon = Amazon()
        response = amazon.search(set_id)
        print(response)
        item = response.find('item')
        print(item)
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
                return new_legoset
            except:
                raise FlaskError('Unable to save new set to database', status_code=500)
        raise FlaskError('Could not find set {} on Amazon'.format(id), status_code=400)


    #  def remove_legoset(self, id)

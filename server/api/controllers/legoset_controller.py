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
    def create_legoset_record(self, set_id):
        ''' 
            Add a legoset to the database
            Presupposes check for pre-existence already done
        '''
        # Query Amazon API for info about the set
        amazon = Amazon()
        response = amazon.search(set_id)
        item = response.find('item')
        if item is not None:
            new_legoset_options = {
                'id': set_id,
                'url': item.find('detailpageurl').get_text(),
                'title': item.find('itemattributes').find('title').get_text(),
                'image': item.find('mediumimage').find('url').get_text()
            }
            new_legoset = LegoSet(new_legoset_options)
            try:
                new_legoset.save()
                return new_legoset.to_dict()
            except:
                raise FlaskError('Unable to save new set to database', status_code=500)
        raise FlaskError('Could not find set {} on Amazon'.format(set_id), status_code=400)
    

    def add_legoset(self, set_id):
        '''
            POST /legoset/add/<id>
            Fetch data about a legoset from Amazon and add to the database 
        '''
        id = str(set_id)
        # Check if set exists already; if so raise an error but also 200 OK response
        set_exists = LegoSet.query.filter_by(id=id).first()
        if set_exists:
            raise FlaskError('Set {} already exists in the database'.format(id), status_code=200)
        new_legoset = self.create_legoset_record(set_id)
        return new_legoset


    #  def remove_legoset(self, id)

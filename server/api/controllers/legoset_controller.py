'''
    /api/controllers/legoset_controller.py
    Controller for legosets
'''
from api.amazon import Amazon
from api.models import LegoSet
from api.errors import FlaskError
from api.controllers.auth_controller import AuthController


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
            new_legoset = LegoSet({
                'id': set_id,
                'url': item.find('detailpageurl').get_text(),
                'title': item.find('itemattributes').find('title').get_text(),
                'image': item.find('mediumimage').find('url').get_text()
            })
            try:
                new_legoset.save()
                return new_legoset.to_dict()
            except:
                raise FlaskError('Unable to save new set to database', status_code=500)
        raise FlaskError('Could not find set {} on Amazon'.format(set_id), status_code=400)
    

    def add_legoset(self, set_id, token):
        '''
            POST /legoset/add/<id>
            Fetch data about a legoset from Amazon and add to the database 
        '''
        user = AuthController.authenticate(token)
        # if user is None:
        #    raise FlaskError('Could not authenticate user', status_code=401)
        id = str(set_id)
        # Check if set exists already; if so raise an error but also 200 OK response
        set_exists = LegoSet.query.filter_by(id=id).first()
        if set_exists:
            raise FlaskError('Set {} already exists in the database'.format(id), status_code=200)
        new_legoset = self.create_legoset_record(set_id)
        return new_legoset

    
    def search(self, set_id, token):
        '''
            GET /legoset/search/<id>
            Queries Amazon for info about this legoset and returns it
        '''
        user = AuthController.authenticate(token)
        # First check in our database
        set_exists = LegoSet.query.filter_by(id=set_id).first()
        if set_exists:
            return set_exists.to_dict()
        # If not found, check amazon
        amazon = Amazon()
        response = amazon.search(set_id)
        item = response.find('item')
        if item is not None:
            return {
                'id': int(set_id),
                'url': item.find('detailpageurl').get_text(),
                'title': item.find('itemattributes').find('title').get_text(),
                'image': item.find('mediumimage').find('url').get_text()
            }
        # If it could not be found, raise an error but also 200 status indicating no fault
        raise FlaskError('Could not find set {} on Amazon'.format(set_id), status_code=200)
    
    
    #  def remove_legoset(self, id)

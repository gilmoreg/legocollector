"""
    /api/controllers/legoset_controller.py
    Controller for legosets
"""
from api.amazon import Amazon
from api.models import LegoSet, StockLevel
from api.errors import FlaskError
from api.controllers.auth_controller import AuthController

print('importing legocontroller')


class LegoSetController(object):
    """
    Controller for legosets
    """
    def __init__(self):
        self.amazon = Amazon()


    @staticmethod
    def get_legosets():
        """ Get all legoset records """
        return LegoSet.query.all()

    def create_legoset_record(self, set_id):
        """
        Add a legoset to the database
        Presupposes check for pre-existence already done
        """
        # Query Amazon API for info about the set
        response = self.amazon.search(set_id)
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
                # Update stock level so we have some inital data to display
                self.update_stock(new_legoset)
                return new_legoset
            except:
                raise FlaskError('Unable to save new set to database', status_code=500)
        raise FlaskError('Could not find set {} on Amazon'.format(set_id), status_code=400)

    def add_legoset(self, set_id, token):
        """
        POST /legoset/add/<id>
        Fetch data about a legoset from Amazon and add to the database
        """
        AuthController.authenticate(token)
        id = str(set_id)
        # Check if set exists already; if so raise an error but also 200 OK response
        set_exists = LegoSet.query.filter_by(id=id).first()
        if set_exists:
            raise FlaskError('Set {} already exists in the database'.format(id), status_code=200)
        new_legoset = self.create_legoset_record(set_id)
        return new_legoset.to_dict()


    def search(self, set_id, token):
        """
        GET /legoset/search/<id>
        Queries Amazon for info about this legoset and returns it
        """
        AuthController.authenticate(token)
        # First check in our database
        set_exists = LegoSet.query.filter_by(id=set_id).first()
        if set_exists:
            return set_exists.to_dict()
        # If not found, check amazon
        response = self.amazon.search(set_id)
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

    @staticmethod
    def cull_stock(legoset):
        """ Keep only the most recent stock levels """
        if len(legoset.stock_levels) > 30:
            # Stock levels already sorted by date
            # Keep only the most recent 29
            legoset.stock_levels[:] = legoset.stock_levels[-30:]
            legoset.save()

    def update_stock(self, legoset):
        """
        Add stock level datapoint for specificed set
        @param legoset - LegoSet instance
        @param amazon - Amazon instance
        """
        self.cull_stock(legoset)
        response = self.amazon.search(legoset.id)
        item = response.find('item')
        if item is not None:
            level = item.find('totalnew').get_text()
            if level is not None:
                stock_level = StockLevel(level)
                legoset.stock_levels.append(stock_level)
                legoset.save()

    def update_stock_by_id(self, set_id):
        """
        Given just a set_id, add stock level datapoint
        @param set_id - int representing set id
        """
        legoset = LegoSet.query.filter_by(id=set_id).first()
        self.update_stock(legoset)

    def update_stock_levels(self):
        """
        Query Amazon for each Legoset in database,
        add a StockLevel datapoint for each one
        """
        print('Updating stock levels')
        legosets = self.get_legosets()
        for legoset in legosets:
            try:
                self.update_stock(legoset)
            except Exception as e:
                print('error updating', legoset, e)

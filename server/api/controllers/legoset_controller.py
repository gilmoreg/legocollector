"""
    /api/controllers/legoset_controller.py
    Controller for legosets
"""
from api.amazon import Amazon
from api.models import LegoSet, StockLevel
from api.errors import FlaskError
from api.controllers.auth_controller import AuthController


class LegoSetController(object):
    """
        Controller for legosets
    """

    @staticmethod
    def get_legosets():
        """ Get all legoset records """
        return LegoSet.query.all()

    @staticmethod
    def create_legoset_record(set_id):
        """
            Add a legoset to the database
            Presupposes check for pre-existence already done
        """
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
                return new_legoset
            except:
                raise FlaskError('Unable to save new set to database', status_code=500)
        raise FlaskError('Could not find set {} on Amazon'.format(set_id), status_code=400)

    def add_legoset(self, set_id, token):
        """
            POST /legoset/add/<id>
            Fetch data about a legoset from Amazon and add to the database
        """
        user = AuthController.authenticate(token)
        if user is None:
            raise FlaskError('Could not authenticate user', status_code=401)
        id = str(set_id)
        # Check if set exists already; if so raise an error but also 200 OK response
        set_exists = LegoSet.query.filter_by(id=id).first()
        if set_exists:
            raise FlaskError('Set {} already exists in the database'.format(id), status_code=200)
        new_legoset = self.create_legoset_record(set_id)
        # Update stock level so we have some inital data to display
        self.update_stock(new_legoset)
        return new_legoset.to_dict()

    @staticmethod
    def search(set_id, token):
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

    @staticmethod
    def cull_stock(legoset):
        """ Keep only the most recent stock levels """
        if len(legoset.stock_levels) > 30:
            # Stock levels already sorted by date
            # Keep only the most recent 29
            legoset.stock_levels[:] = legoset.stock_levels[-30:]
            legoset.save()

    def update_stock(self, legoset, amazon=Amazon()):
        """
        Add stock level datapoint for specificed set
        @param legoset - LegoSet instance
        @param amazon - Amazon instance
        """
        self.cull_stock(legoset)
        response = amazon.search(legoset.id)
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
        self.update_stock(legoset, Amazon())

    def update_stock_levels(self):
        """
        Query Amazon for each Legoset in database,
        add a StockLevel datapoint for each one
        This function runs on a schedule set up in api/schedule.py
        """
        legosets = self.get_legosets()
        amazon = Amazon()
        for legoset in legosets:
            try:
                self.update_stock(legoset, amazon)
            except:
                pass

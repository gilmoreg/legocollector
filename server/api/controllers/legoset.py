"""
    /api/controllers/legoset_controller.py
    Controller for legosets
"""
from api.amazon import Amazon
from api.errors import FlaskError
from api.models import LegoSet, StockLevel


amazon = Amazon()


def get_legosets():
    """ Get all legoset records """
    return LegoSet.query.all()


def get_or_create_legoset(set_id):
    """ Return LegoSet. Create one if it does not exist yet. """
    set_exists = LegoSet.query.filter_by(id=set_id).first()
    if set_exists:
        return set_exists
    new_set = create_legoset_record(set_id)
    return new_set


def create_legoset_record(set_id):
    """
    Add a legoset to the database
    Presupposes check for pre-existence already done
    """
    # Query Amazon API for info about the set
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
            # Update stock level so we have some inital data to display
            update_stock(new_legoset)
            return new_legoset
        except:
            raise FlaskError('Unable to save new set to database', status_code=500)
    raise FlaskError('Could not find set {} on Amazon'.format(set_id), status_code=400)


def search(set_id):
    """
    GET /legoset/search/<id>
    Queries Amazon for info about this legoset and returns it
    """
    # First check in our database
    set_exists = LegoSet.query.filter_by(id=set_id).first()
    if set_exists:
        return set_exists.to_dict()
    # If not found, check amazon
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


def update_stock(legoset):
    """
    Add stock level datapoint for specificed set
    @param legoset - LegoSet instance
    """
    legoset.cull_stock()
    response = amazon.search(legoset.id)
    item = response.find('item')
    if item is not None:
        level = item.find('totalnew').get_text()
        if level is not None:
            stock_level = StockLevel(level)
            legoset.stock_levels.append(stock_level)
            legoset.save()


def update_stock_by_id(set_id):
    """
    Given just a set_id, add stock level datapoint
    @param set_id - int representing set id
    """
    legoset = LegoSet.query.filter_by(id=set_id).first()
    update_stock(legoset)


def update_stock_levels():
    """
    Query Amazon for each Legoset in database,
    add a StockLevel datapoint for each one
    """
    print('Updating stock levels')
    legosets = get_legosets()
    for legoset in legosets:
        try:
            update_stock(legoset)
        except Exception as e:
            print('error updating', legoset, e)

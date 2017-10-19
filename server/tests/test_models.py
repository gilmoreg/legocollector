""" Tests for models """
import pytest

from api.models import User, LegoSet, StockLevel


@pytest.mark.usefixtures('db')
class TestUser:
    """ Tests for User model """

    def test_creation(self):
        user = User('test@test.com')
        user.save()
        retrieved = User.query.filter_by(email='test@test.com').first()
        assert retrieved == user
        json = retrieved.to_dict()
        assert json['email'] == 'test@test.com'


@pytest.mark.usefixtures('db')
class TestLegoSet:
    """ Tests for LegoSet model """

    def test_creation(self):
        legoset = LegoSet({
            'id': 12345,
            'title': 'test',
            'image': 'test',
            'url': 'test',
        })
        legoset.save()
        retrieved = LegoSet.query.filter_by(id=12345).first()
        assert retrieved == legoset

    def test_create_with_user(self):
        """ Attach a set to a user """
        legoset = LegoSet({
            'id': 12345,
            'title': 'test',
            'image': 'test',
            'url': 'test',
        }).save()
        user = User('test@test.com')
        user.watches.append(legoset)
        user.save()
        retrieved = User.query.first()
        assert retrieved.watches[0] == legoset


@pytest.mark.usefixtures('db')
class TestStockLevel:
    """ Tests for StockLevel model """

    def test_creation(self):
        legoset = LegoSet({
            'id': 12345,
            'title': 'test',
            'image': 'test',
            'url': 'test',
        }).save()
        stock_level = StockLevel(999).save()
        legoset.stock_levels.append(stock_level)
        legoset.save()
        retrieved_stock_level = legoset.stock_levels[0]
        assert retrieved_stock_level == stock_level

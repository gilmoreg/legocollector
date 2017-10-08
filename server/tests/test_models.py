''' Tests for models '''
import pytest
from api.models import User, LegoSet, Watch, StockLevel


@pytest.mark.usefixtures('db')
class TestUser:
    ''' Tests for User model '''
    def test_creation(self):
        user = User('test@test.com')
        user.save()
        retrieved = User.query.filter_by(email='test@test.com').first()
        assert retrieved == user
        json = retrieved.to_dict()
        assert json['email'] == 'test@test.com'


@pytest.mark.usefixtures('db')
class TestLegoSet:
    ''' Tests for LegoSet model '''
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


@pytest.mark.usefixtures('db')
class TestWatch:
    ''' Tests for Watch model '''
    def test_creation(self):
        user = User('test@test.com')
        user.save()
        legoset = LegoSet({
            'id': 12345,
            'title': 'test',
            'image': 'test',
            'url': 'test',
        })
        legoset.save()
        watch = Watch(user.id, legoset.id)
        watch.save()
        retrieved = Watch.query.filter_by(id=watch.id).first()
        assert retrieved == watch


@pytest.mark.usefixtures('db')
class TestStockLevel:
    ''' Tests for StockLevel model '''
    def test_creation(self):
        legoset = LegoSet({
            'id': 12345,
            'title': 'test',
            'image': 'test',
            'url': 'test',
        })
        legoset.save()
        stock_level = StockLevel(legoset.id, 0)
        stock_level.save()
        retrieved = StockLevel.query.filter_by(id=stock_level.id).first()
        assert retrieved == stock_level
        json = retrieved.to_dict()
        assert json['lego_set'] == 12345
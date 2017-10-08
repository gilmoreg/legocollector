''' Tests for watch controller '''
import pytest
from unittest.mock import Mock, patch
from api.amazon import Amazon
from api.controllers.watch_controller import WatchController
from api.controllers.auth_controller import AuthController
from api.models import LegoSet, Watch, User
from api.errors import FlaskError
from ..testutils import bottlenose_mock_empty, bottlenose_mock_success


class TestWatchController:
    ''' Tests for WatchController '''
    @pytest.mark.usefixtures('db')
    def test_get_all_watches(self, client):
        ''' Test get_all_watches '''
        watch_controller = WatchController()
        watches = watch_controller.get_all_watches()
        assert watches == []


    @pytest.mark.usefixtures('db')
    def test_get_watch(self, client):
        ''' Test get_watch '''
        watch_controller = WatchController()
        token = AuthController.create_jwt('test@test.com')
        user = User('test@test.com')
        user.save()
        legoset = LegoSet({
            'id': 12345,
            'title': 'Test Lego Set',
            'image': 'test',
            'url': 'test'
        })
        legoset.save()
        watch = Watch(user.id, legoset.id)
        watch.save()
        retreived = watch_controller.get_watch(watch.id, token)
        assert retreived['id'] == watch.id
        assert retreived['user'] == watch.user
        assert retreived['lego_set'] == watch.lego_set
        

    
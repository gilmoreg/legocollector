''' Tests for watch controller '''
import pytest
from unittest.mock import Mock, patch
from api.amazon import Amazon
from api.controllers.watch_controller import WatchController
from api.controllers.auth_controller import AuthController
from api.models import LegoSet, Watch, User
from api.errors import FlaskError
from ..testutils import bottlenose_mock_empty, bottlenose_mock_success
from ..factories import create_user, create_legoset, create_watch

class TestWatchController:
    ''' Tests for WatchController '''
    @pytest.mark.usefixtures('db')
    def test_get_all_watches(self, client):
        ''' Test get_all_watches '''
        watch_controller = WatchController()
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        watch = create_watch(user['id'], legoset['id'])
        watches = watch_controller.get_users_watches(user['token'])
        assert len(watches) == 1
        watch_1 = watches[0]
        assert watch_1['id'] == 1
        assert watch_1['lego_set'] == 12345 


    @pytest.mark.usefixtures('db')
    def test_get_watch(self, client):
        ''' Test get_watch '''
        watch_controller = WatchController()
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        watch = create_watch(user['id'], legoset['id'])
        watches = watch_controller.get_users_watches(user['token'])
        retreived = watch_controller.get_watch(watch['id'], user['token'])
        assert retreived['id'] == watch['id']
        assert retreived['user'] == watch['user']
        assert retreived['lego_set'] == watch['lego_set']
        

    
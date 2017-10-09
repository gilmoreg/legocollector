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
    watch_controller = WatchController()

    @pytest.mark.usefixtures('db')
    def test_get_all_watches(self, client):
        ''' Test get_all_watches '''
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        watch = create_watch(user['id'], legoset['id'])
        watches = self.watch_controller.get_users_watches(user['token'])
        assert len(watches) == 1
        watch_1 = watches[0]
        assert watch_1['id'] == 1
        assert watch_1['lego_set'] == 12345 


    @pytest.mark.usefixtures('db')
    def test_get_watch(self, client):
        ''' Test get_watch '''
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        watch = create_watch(user['id'], legoset['id'])
        retreived = self.watch_controller.get_watch(watch['id'], user['token'])
        assert retreived['id'] == watch['id']
        assert retreived['user'] == watch['user']
        assert retreived['lego_set'] == watch['lego_set']


    @pytest.mark.usefixtures('db')
    def test_get_watch_not_exists(self, client):
        ''' Test get_watch for nonexistent watch '''
        user = create_user('test@test.com')
        try:
            retrieved = self.watch_controller.get_watch(0, user['token'])
        except FlaskError as e:
            assert e.to_dict() == {'message': 'Watch not found', 'status_code': 400}

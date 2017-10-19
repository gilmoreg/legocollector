""" Tests for watch controller """
import pytest
# noinspection PyCompatibility
from unittest.mock import Mock, patch
from api.amazon import Amazon
from api.controllers.watch_controller import WatchController
from api.controllers.auth_controller import AuthController
from api.errors import FlaskError
from ..testutils import bottlenose_mock_empty, bottlenose_mock_success
from ..factories import create_user, create_legoset, create_watch


class TestWatchController:
    """ Tests for WatchController """
    watch_controller = WatchController()

    @pytest.mark.usefixtures('db')
    def test_get_all_watches(self, client):
        """ Test get_all_watches """
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        watch = create_watch(user['user'], legoset)
        watches = self.watch_controller.get_users_watches(user['token'])
        assert len(watches) == 1
        watch_1 = watches[0]
        assert watch_1['id'] == 12345
        assert len(watch_1['stock_levels']) == 0 

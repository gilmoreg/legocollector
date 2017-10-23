""" Tests for watch controller """
import pytest

# noinspection PyCompatibility
from api.controllers.auth_controller import AuthController
from api.controllers.legoset_controller import LegoSetController
from api.controllers.watch_controller import WatchController
from ..factories import create_user, create_legoset, create_watch


class TestWatchController:
    """ Tests for WatchController """
    watch_controller = WatchController(AuthController(), LegoSetController())

    @pytest.mark.usefixtures('db')
    def test_get_all_watches(self):
        """ Test get_all_watches """
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        create_watch(user['user'], legoset)
        watches = self.watch_controller.get_users_watches(user['token'])
        assert len(watches) == 1
        watch_1 = watches[0]
        assert watch_1['id'] == 12345
        assert len(watch_1['stock_levels']) == 0

    @pytest.mark.usefixtures('db')
    def test_delete_watch(self):
        """ Confirm removal of watch """
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        create_watch(user['user'], legoset)
        assert len(user['user'].watches) == 1
        WatchController.delete_watch(user['token'], 12345)
        assert len(user['user'].watches) == 0

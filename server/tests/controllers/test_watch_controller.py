""" Tests for watch controller """
import pytest

# noinspection PyCompatibility
import api.controllers.watch as watch_controller
from api.errors import FlaskError
from ..factories import create_user, create_legoset, create_watch


class TestWatchController:
    """ Tests for WatchController """
    @pytest.mark.usefixtures('db')
    def test_get_all_watches(self):
        """ Test get_all_watches """
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        create_watch(legoset, user['user'])
        watches = watch_controller.get_users_watches(user['user'])
        assert len(watches) == 1
        watch_1 = watches[0]
        assert watch_1['id'] == 12345
        assert len(watch_1['stock_levels']) == 0

    @pytest.mark.usefixtures('db')
    def test_delete_watch(self):
        """ Confirm removal of watch """
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        create_watch(legoset, user['user'])
        assert len(user['user'].watches) == 1
        watch_controller.delete_watch(12345, user['user'])
        assert len(user['user'].watches) == 0

    @pytest.mark.usefixtures('db')
    def test_duplicate_watch(self):
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        watch_controller.add_watch(legoset, user['user'])
        try:
            watch_controller.add_watch(legoset, user['user'])
        except FlaskError as e:
            assert e.to_dict() == {'message': 'Watch already exists for user', 'status_code': 400}

""" Tests for /watch views """
import pytest
# noinspection PyCompatibility
from unittest.mock import Mock, patch
from ..testutils import decode_json, post_json, create_jwt, \
    create_bad_jwt, bottlenose_mock_success, bottlenose_mock_empty
from ..factories import create_user
from api.models import User
from api.amazon import Amazon


@pytest.mark.usefixtures('db')
class TestWatchViews:
    """ Tests for /watch views """

    def test_get_users_watches(self, client):
        """ Verify 200 status and empty response with no watches in db """
        user = create_user('test@test.com')
        response = client.get('/watches?token=' + user['token'])
        json = decode_json(response)
        assert response.status_code == 200
        assert json == {'result': []}

    def test_add_watch(self, client):
        """ Verify existence of test watch after adding """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            response = post_json(client, '/watches/add', {'token': user['token'], 'id': '54321'})
            json = decode_json(response)['result']
            assert json['id'] == 54321
            assert len(json['stock_levels']) == 0

    def test_watch_empty_search(self, client):
        """ Verify behavior when Amazon search returns empty """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty

        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            response = post_json(client, '/watches/add', {'token': user['token'], 'id': '54321'})
            json = decode_json(response)
            assert json == {'error': 'Could not find set 54321 on Amazon'}

    def test_watch_no_token(self, client):
        response = post_json(client, '/watches/add', {'id': '54321'})
        json = decode_json(response)
        assert json == {'error': 'Must supply a token and a set ID'}

    def test_watch_bad_token(self, client):
        token = create_bad_jwt()
        response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

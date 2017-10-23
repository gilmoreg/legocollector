""" Tests for /watch views """
# noinspection PyCompatibility
from unittest.mock import Mock, patch

import pytest

from api.amazon import Amazon
from ..factories import create_user, create_legoset, create_watch
from ..testutils import decode_json, post_json, create_bad_jwt, bottlenose_mock_success, bottlenose_mock_empty


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

    def test_get_watches_no_token(self, client):
        response = client.get('/watches')
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

    def test_get_watches_bad_token(self, client):
        token = create_bad_jwt()
        response = client.get('/watches?token=' + token)
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

    def test_get_watch(self, client):
        """ get_watch() """
        user = create_user('test@test.com')
        legoset = create_legoset(12345)
        create_watch(user['user'], legoset)
        response = client.get('/watches/12345?token=' + user['token'])
        json = decode_json(response)['result']
        assert json['id'] == 12345

    def test_get_watch_no_token(self, client):
        response = client.get('/watches/12345')
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

    def test_get_watch_bad_token(self, client):
        token = create_bad_jwt()
        response = client.get('/watches/12345?token=' + token)
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

    def test_add_watch(self, client):
        """ Verify existence of test watch after adding """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            response = post_json(client, '/watches/add', {'token': user['token'], 'id': '54321'})
            json = decode_json(response)['result']
            assert json['id'] == 54321
            assert len(json['stock_levels']) == 1

    def test_watch_empty_search(self, client):
        """ Verify behavior when Amazon search returns empty """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            response = post_json(client, '/watches/add', {'token': user['token'], 'id': '54321'})
            json = decode_json(response)
            assert json == {'error': 'Could not find set 54321 on Amazon'}

    def test_add_watch_no_token(self, client):
        response = post_json(client, '/watches/add', {'id': '54321'})
        json = decode_json(response)
        assert json == {'error': 'Must supply a token and a set ID'}

    def test_add_watch_bad_token(self, client):
        token = create_bad_jwt()
        response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

    def test_delete_watch(self, client):
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            legoset = create_legoset(12345)
            create_watch(user['user'], legoset)
            response = post_json(client, '/watches/delete/12345', {'token': user['token']})
            json = decode_json(response)
            assert json == {'result': 'Watch 12345 deleted'}

    def test_delete_watch_empty(self, client):
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            response = post_json(client, '/watches/delete/12345', {'token': user['token']})
            json = decode_json(response)
            assert json == {'error': 'Watch not found'}

    def test_delete_watch_no_token(self, client):
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        with patch.object(Amazon, 'search', mock_bottlenose):
            response = post_json(client, '/watches/delete/12345', {})
            json = decode_json(response)
            assert json == {'error': 'Must supply a token and a set ID'}


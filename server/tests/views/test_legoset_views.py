""" Tests for legoset views """
import pytest
# noinspection PyCompatibility
from unittest.mock import Mock, patch
from ..testutils import decode_json, post_json, create_jwt, \
    create_bad_jwt, bottlenose_mock_success, bottlenose_mock_empty, \
    create_admin_jwt
from ..factories import create_legoset, create_user, create_watch
from api.amazon import Amazon


@pytest.mark.usefixtures('db')
class TestLegosetViews:
    """ Tests for /legoset """
    def test_search(self, client):
        """ Test searching for a set with success """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            response = client.get('/legoset/search/12345?token=' + token)
            json = decode_json(response)['result']
            assert json['id'] == 12345

    def test_search_preexisting(self, client):
        """ Test search already stored set """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            post_json(client, '/legoset/add/12345', {'token': token})
            response = client.get('/legoset/search/12345?token=' + token)
            json = decode_json(response)['result']
            assert json['id'] == 12345

    def test_search_invalid_query(self, client):
        """ Test query with invalid characters """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            post_json(client, '/legoset/add/12345', {'token': token})
            response = client.get('/legoset/search/abcdef?token=' + token)
            json = decode_json(response)
            assert json == {'error': 'Please supply a valid query (a 5 to 7 digit integer)'}

    def test_search_empty(self, client):
        """ Test search with no amazon results """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            post_json(client, '/legoset/add/12345', {'token': token})
            response = client.get('/legoset/search/12345?token=' + token)
            json = decode_json(response)
            assert json == {'error': 'Could not find set 12345 on Amazon'}

    def test_search_missing_token(self, client):
        """ Test search with missing token """
        response = client.get('/legoset/search/12345')
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}

    def test_search_bad_token(self, client):
        """ Test search with an invalid token """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        token = create_bad_jwt()
        with patch.object(Amazon, 'search', mock_bottlenose):
            response = client.get('/legoset/search/12345?token=' + token)
            json = decode_json(response)
            assert json == {'error': 'Could not authenticate user'}

    def test_udpate(self, client):
        """ Test update stock endpoint """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        admin = create_admin_jwt()
        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            legoset = create_legoset(12345)
            create_watch(legoset, user['user'])
            post_json(client, '/legoset/update', {'token': admin})
            response = client.get('/legoset/search/12345?token=' + user['token'])
            json = decode_json(response)['result']
            assert len(json['stock_levels']) == 1

    def test_update_bad_token(self, client):
        token = create_bad_jwt()
        response = post_json(client, '/legoset/update', {'token': token})
        json = decode_json(response)['result']
        assert json == 'unauthorized'

    def test_update_bad_amazon_response(self, client):
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        admin = create_admin_jwt()
        with patch.object(Amazon, 'search', mock_bottlenose):
            user = create_user('test@test.com')
            legoset = create_legoset(12345)
            create_watch(legoset, user['user'])
            post_json(client, '/legoset/update', {'token': admin})
            response = client.get('/legoset/search/12345?token=' + user['token'])
            json = decode_json(response)['result']
            assert len(json['stock_levels']) == 0

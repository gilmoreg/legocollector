""" Tests for legoset views """
import pytest
# noinspection PyCompatibility
from unittest.mock import Mock, patch
from ..testutils import decode_json, post_json, create_jwt, \
    create_bad_jwt, bottlenose_mock_success, bottlenose_mock_empty
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

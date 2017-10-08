''' Tests for views '''
import pytest
from unittest.mock import Mock, patch
from ..testutils import decode_json, post_json, create_jwt, create_bad_jwt, bottlenose_mock_success, bottlenose_mock_empty
from api.amazon import Amazon


@pytest.mark.usefixtures('db')
class TestLegosetViews:
    ''' Tests for /legoset '''
    def test_add_legoset(self, client):
        ''' Test /legoset/add/<id> '''
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            response = post_json(client, '/legoset/add/12345', {'token': token})
            json = decode_json(response)['result']
            assert json['id'] == 12345
            assert json['image'] == 'https://images-na.ssl-images-amazon.com/images/I/Test._SL160_.jpg'
            assert json['title'] == 'Test Set Title'
            assert json['url'] == 'https://amazon.com/test_setname/dp/TESTASIN00'


    def test_add_empty_search(self, client):
        ''' Test add invalid set id '''
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            response = post_json(client, '/legoset/add/12345', {'token': token})
            json = decode_json(response)
            assert json == {'error': 'Could not find set 12345 on Amazon'}

    
    def test_missing_token(self, client):
        ''' Test without token '''
        response = post_json(client, '/legoset/add/12345', {})
        json = decode_json(response)
        assert json == {'error': 'Must supply a set_id and a valid token'}


    def test_bad_token(self, client):
        ''' Test with a bad token '''
        token = create_bad_jwt()
        response = post_json(client, '/legoset/add/12345', {'token': token})
        json = decode_json(response)
        assert json == {'error': 'Could not authenticate user'}


    def test_duplicate_add(self, client):
        ''' Test adding existing set '''
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        token = create_jwt('54321')
        with patch.object(Amazon, 'search', mock_bottlenose):
            post_json(client, '/legoset/add/12345', {'token': token})
            response = post_json(client, '/legoset/add/12345', {'token': token})
            json = decode_json(response)
            assert json == {'error': 'Set 12345 already exists in the database'}


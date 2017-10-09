''' Tests for /watch views '''
import pytest
from unittest.mock import Mock, patch
from ..testutils import decode_json, post_json, create_jwt, create_bad_jwt, bottlenose_mock_success, bottlenose_mock_empty
from api.models import User
from api.amazon import Amazon


@pytest.mark.usefixtures('db')
class TestWatchViews:
    ''' Tests for /watch views '''
    def test_get_users_watches(self, client):
        ''' Verify 200 status and empty response with no watches in db '''
        token = create_jwt('test@test.com')
        user = User('test@test.com')
        user.save()
        response = client.get('/watches?token=' + token)
        json = decode_json(response)
        print(json)
        assert response.status_code == 200
        assert json == {'result': []}


    def test_add_watch(self, client):
        ''' Verify existence of test watch after adding '''
        token = create_jwt('12345')
        
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
            json = decode_json(response)['result']
            assert json['id'] == 1
            assert json['lego_set'] == 54321
            assert json['user'] == 12345

     
    def test_watch_empty_search(self, client):
        ''' Verify behavior when Amazon search returns empty '''
        token = create_jwt('12345')
        
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_empty

        with patch.object(Amazon, 'search', mock_bottlenose):
            response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
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



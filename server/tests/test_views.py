''' Tests for views '''
import pytest
from unittest.mock import Mock, patch
from flask import g
from .testutils import decode_json, post_json, create_jwt, bottlenose_mock_success
from api.amazon import Amazon


class TestWatchViews:
    ''' Tests for /watch views '''

    @pytest.mark.usefixtures('db')
    def test_get_watches(self, client):
        ''' Verify 200 status and empty response with no watches in db '''
        response = client.get('/watches')
        json = decode_json(response)
        assert response.status_code == 200
        assert json == {'result': []}


    @pytest.mark.usefixtures('db')
    def test_add_watch(self, client):
        ''' Verify existence of test watch after adding '''
        token = create_jwt('12345')
        
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
            json = decode_json(response)['result']
            print(json)
            assert json['id'] == 1
            assert json['lego_set'] == 54321
            assert json['user'] == 12345

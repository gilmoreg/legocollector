''' Tests for views '''
import pytest
from unittest import mock
from flask import g
from .testutils import decode_json, post_json, create_jwt, bottlenose_mock_success


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
        mocker.patch('g.amazon', new_callable=bottlenose_mock_success)
        response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
        json = decode_json(response)
        print(json)
        assert 0

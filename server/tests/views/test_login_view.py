''' Tests for login views '''
import pytest
from unittest.mock import Mock, patch
import requests
from ..testutils import post_json, decode_json, amazon_fail, amazon_success


@pytest.mark.usefixtures('db')
class TestLoginView():
    ''' Tests for /login '''
    def test_login(self, client):
        ''' Test /login success '''
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = amazon_success

        with patch.object(requests, 'get', mock_amazon):
            response = post_json(client, '/login', {
                'access_token': 'test_token'
            })
            json = decode_json(response)['result']
            assert json['email'] == 'test@test.com'

    def test_login_fail(self, client):
        ''' Test with amazon fail response'''
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = amazon_fail

        with patch.object(requests, 'get', mock_amazon):
            response = post_json(client, '/login', {
                'access_token': 'test_token'
            })
            json = decode_json(response)
            assert json == {'error': 'Could not authenticate user'}

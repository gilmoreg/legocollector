""" Tests for login views """
import pytest
# noinspection PyCompatibility
from unittest.mock import Mock, patch
import requests
from ..testutils import post_json, decode_json, AmazonFail, AmazonSuccess


@pytest.mark.usefixtures('db')
class TestLoginView:
    """ Tests for /login """
    def test_wake(self, client):
        response = client.get('/')
        json = decode_json(response)
        assert json == {'result': 'success'}

    def test_login(self, client):
        """ Test /login success """
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = AmazonSuccess

        with patch.object(requests, 'get', mock_amazon):
            response = post_json(client, '/login', {
                'access_token': 'test_token'
            })
            json = decode_json(response)['result']
            assert json['email'] == 'test@test.com'

    def test_login_fail(self, client):
        """ Test with amazon fail response"""
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = AmazonFail

        with patch.object(requests, 'get', mock_amazon):
            response = post_json(client, '/login', {
                'access_token': 'test_token'
            })
            print('response', response)
            json = decode_json(response)
            assert json == {'error': 'Could not authenticate user'}

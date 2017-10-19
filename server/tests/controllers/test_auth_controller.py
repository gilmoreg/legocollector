""" Tests for legoset controller """
# noinspection PyCompatibility
from unittest.mock import Mock, patch

import pytest
import requests

from api.controllers.auth_controller import AuthController
from api.errors import FlaskError
from api.models import User
from ..factories import create_user
from ..testutils import AmazonSuccess, AmazonFail


@pytest.mark.usefixtures('db')
class TestAuthController:
    """ Tests for AuthController """
    def test_create_jwt(self):
        auth_controller = AuthController()
        token = auth_controller.create_jwt(12345)
        assert isinstance(token, str)

    def test_login_success_new_user(self):
        """ Test login new user with mocked successful Amazon response """
        auth_controller = AuthController()
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = AmazonSuccess

        with patch.object(requests, 'get', mock_amazon):
            response = auth_controller.login('test_token')
            assert response['email'] == 'test@test.com'

    def test_login_success_existing_user(self):
        """ Test login existing user """
        user = User('test@test.com')
        user.save()
        auth_controller = AuthController()
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = AmazonSuccess

        with patch.object(requests, 'get', mock_amazon):
            response = auth_controller.login('test_token')
            assert response['email'] == 'test@test.com'

    def test_login_fail(self):
        """ Test with fail response from Amazon """
        auth_controller = AuthController()
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = AmazonFail

        with patch.object(requests, 'get', mock_amazon):
            try:
                response = auth_controller.login('test_token')
            except FlaskError as e:
                assert e.to_dict() == {
                    'message': 'Could not authenticate user',
                    'status_code': 401
                }

    def test_get_user(self):
        user = create_user('test@test.com')
        auth_controller = AuthController()
        retrieved = auth_controller.get_user(user['token']).to_dict()
        assert retrieved['id'] == user['user'].id
        assert retrieved['email'] == user['email']

    def test_get_user_notfound(self):
        auth_controller = AuthController()
        try:
            token = AuthController.create_jwt('test@test.com')
            retrieved = auth_controller.get_user(token).to_dict()
        except FlaskError as e:
            assert e.to_dict() == {'message': 'User not found', 'status_code': 401}

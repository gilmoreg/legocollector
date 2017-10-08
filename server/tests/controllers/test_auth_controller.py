''' Tests for legoset controller '''
import pytest
from unittest.mock import Mock, patch
import requests
from api.controllers.auth_controller import AuthController
from api.models import User
from api.errors import FlaskError
from ..testutils import amazon_success, amazon_fail


@pytest.mark.usefixtures('db')
class TestAuthController:
    ''' Tests for AuthController '''
    def test_create_jwt(self):
        auth_controller = AuthController()
        token = auth_controller.create_jwt(12345)
        assert isinstance(token, str)

    
    def test_login_success_new_user(self):
        ''' Test login new user with mocked successful Amazon response '''
        auth_controller = AuthController()
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = amazon_success

        with patch.object(requests, 'get', mock_amazon):
            response = auth_controller.login('test_token')
            assert response['email'] == 'test@test.com'


    def test_login_success_existing_user(self):
        ''' Test login existing user '''
        user = User('test@test.com')
        user.save()
        auth_controller = AuthController()
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = amazon_success

        with patch.object(requests, 'get', mock_amazon):
            response = auth_controller.login('test_token')
            assert response['email'] == 'test@test.com'

    
    def test_login_fail(self):
        ''' Test with fail response from Amazon '''
        auth_controller = AuthController()
        mock_amazon = Mock(name='get')
        mock_amazon.return_value = amazon_fail

        with patch.object(requests, 'get', mock_amazon):
            try:
                response = auth_controller.login('test_token')
            except Exception as e:
                assert isinstance(e, FlaskError)
                assert e.to_dict() == {
                    'message': 'Could not authenticate user',
                    'status_code': 401
                }
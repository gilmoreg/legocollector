''' Tests for views '''
import pytest
from .testutils import decode_json, post_json
from api.controllers.auth_controller import create_jwt

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
        response = post_json(client, '/watches/add', {'token': token, 'id': '54321'})
        # json = decode_json(response)
        assert 0

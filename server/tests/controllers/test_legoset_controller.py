''' Tests for legoset controller '''
import pytest
from unittest.mock import Mock, patch
from api.amazon import Amazon
from api.controllers.legoset_controller import LegoSetController
from api.errors import FlaskError
from ..testutils import bottlenose_mock_empty, bottlenose_mock_success


class TestLegoSetController:
    ''' Tests for LegoSetController '''
    @pytest.mark.usefixtures('db')
    def test_create_record(self, client):
        ''' create_legoset_record() '''
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345)
            assert legoset['id'] == 12345
            assert legoset['title'] == 'Test Set Title'


    # Fixture omitted to make db fail
    def test_db_fail(self, client):
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            try:
                legoset = legoset_controller.create_legoset_record(12345)
            except Exception as e:
                assert isinstance(e, FlaskError)
                assert e.to_dict() == {
                    'message': 'Unable to save new set to database',
                    'status_code': 500
                }
    
    
    @pytest.mark.usefixtures('db')
    def test_duplicate_record(self, client):
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            try:
                legoset1 = legoset_controller.create_legoset_record(12345)
                legoset2 = legoset_controller.create_legoset_record(12345)
            except Exception as e:
                assert isinstance(e, FlaskError)
                assert e.to_dict() == {
                    'message': 'Unable to save new set to database',
                    'status_code': 500
                }

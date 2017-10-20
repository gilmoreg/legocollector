""" Tests for legoset controller """
# noinspection PyCompatibility
from unittest.mock import Mock, patch

import pytest

from api.amazon import Amazon
from api.controllers.legoset_controller import LegoSetController
from api.errors import FlaskError
from ..testutils import bottlenose_mock_success, create_bad_jwt


class TestLegoSetController:
    """ Tests for LegoSetController """
    @pytest.mark.usefixtures('db')
    def test_create_record(self):
        """ create_legoset_record() """
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345).to_dict()
            assert legoset['id'] == 12345
            assert legoset['title'] == 'Test Set Title'

    @pytest.mark.usefixtures('db')
    def test_failed_auth_add_legoset(self):
        """ add_legoset() """
        legoset_controller = LegoSetController()
        bad_token = create_bad_jwt()
        try:
            legoset_controller.add_legoset(set_id=12345, token=bad_token)
        except FlaskError as e:
            assert e.to_dict() == {'message': 'Could not authenticate user', 'status_code': 401}

    # Fixture omitted to make db fail
    def test_db_fail(self):
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            try:
                legoset_controller.create_legoset_record(12345)
            except FlaskError as e:
                assert e.to_dict() == {
                    'message': 'Unable to save new set to database',
                    'status_code': 500
                }

    @pytest.mark.usefixtures('db')
    def test_duplicate_record(self):
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            try:
                legoset_controller.create_legoset_record(12345)
                legoset_controller.create_legoset_record(12345)
            except FlaskError as e:
                assert e.to_dict() == {
                    'message': 'Unable to save new set to database',
                    'status_code': 500
                }

    @pytest.mark.usefixtures('db')
    def test_udpate_stock_levels(self):
        """ Test updating stock levels """
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset_controller.create_legoset_record(12345)
            legoset_controller.create_legoset_record(54321)
            legoset_controller.update_stock_levels()
            legosets = legoset_controller.get_legosets()
            assert len(legosets[0].stock_levels) == 1
            assert len(legosets[1].stock_levels) == 1

    @pytest.mark.usefixtures('db')
    def test_update_stock_by_id(self):
        """ update_stock_by_id() """
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345)
            legoset_controller.update_stock_by_id(12345)
            assert len(legoset.stock_levels) == 1

    @pytest.mark.usefixtures('db')
    def test_cull_stock(self):
        """ cull_stock() """
        legoset_controller = LegoSetController()
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345)
            # Add over 30 stock levels
            for i in range(0, 35):
                legoset_controller.update_stock_levels()
            legoset_controller.cull_stock(legoset)
            # Ensure only 30 remain
            assert len(legoset.stock_levels) == 30


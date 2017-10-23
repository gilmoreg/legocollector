""" Tests for legoset controller """
# noinspection PyCompatibility
from unittest.mock import Mock, patch

import pytest

import api.controllers.legoset as legoset_controller
from api.amazon import Amazon
from api.errors import FlaskError
from ..testutils import bottlenose_mock_success, create_bad_jwt


class TestLegoSetController:
    """ Tests for LegoSetController """
    @pytest.mark.usefixtures('db')
    def test_create_record(self):
        """ create_legoset_record() """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success

        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345).to_dict()
            assert legoset['id'] == 12345
            assert legoset['title'] == 'Test Set Title'

    # Fixture omitted to make db fail
    def test_db_fail(self):
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
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset_controller.create_legoset_record(12345)
            legoset_controller.create_legoset_record(54321)
            legoset_controller.update_stock_levels()
            legosets = legoset_controller.get_legosets()
            # Initial on creation plus one extra
            assert len(legosets[0].stock_levels) == 2
            assert len(legosets[1].stock_levels) == 2

    @pytest.mark.usefixtures('db')
    def test_update_stock_by_id(self):
        """ update_stock_by_id() """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345)
            legoset_controller.update_stock_by_id(12345)
            # Initial on creation plus one extra
            assert len(legoset.stock_levels) == 2

    @pytest.mark.usefixtures('db')
    def test_cull_stock(self):
        """ cull_stock() """
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            legoset = legoset_controller.create_legoset_record(12345)
            # Add over 30 stock levels
            for i in range(0, 35):
                legoset_controller.update_stock_levels()
            # Ensure only 31 remain
            assert len(legoset.stock_levels) == 31


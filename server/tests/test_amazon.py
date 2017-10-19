""" Tests for Amazon """
# noinspection PyCompatibility
from unittest.mock import Mock, patch
from urllib.error import HTTPError

import pytest

from api.amazon import Amazon
from .testutils import bottlenose_mock_success


@pytest.mark.usefixtures('db')
class TestAmazon:
    """ Tests for the Amazon Module """
    def test_search(self):
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            amazon = Amazon()
            response = amazon.search(12345)
            title = response.find('title').get_text()
            assert title == 'Test Set Title'

    def test_error_handler_503(self):
        """ Test that 503 errors return True """
        amazon = Amazon()
        assert amazon.error_handler(err={
            'exception': HTTPError('/', 503, 'Not available', None, None)
        }) == True

    def test_error_handler_other(self):
        """ Test that non-503 errors return False """
        amazon = Amazon()
        assert amazon.error_handler(err={
            'exception': HTTPError('/', 500, None, None, None)
        }) == False

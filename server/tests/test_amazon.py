''' Tests for Amazon '''
import pytest
from unittest.mock import Mock, patch
from .testutils import bottlenose_mock_success, bottlenose_mock_empty
from api.amazon import Amazon

@pytest.mark.usefixtures('db')
class TestAmazon:
    ''' Tests for the Amazon Module '''
    def test_search(self):
        mock_bottlenose = Mock(name='search')
        mock_bottlenose.return_value = bottlenose_mock_success
        with patch.object(Amazon, 'search', mock_bottlenose):
            amazon = Amazon()
            response = amazon.search(12345)
            title = response.find('title').get_text()
            assert title == 'Test Set Title'




''' Tests for models '''
import pytest
from api.models import User, LegoSet, Watch, StockLevel


@pytest.mark.usefixtures('db')
class TestModels:
    
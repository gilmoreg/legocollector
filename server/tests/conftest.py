''' 
Configure test suite 

Test run command:
py.test --cov-report term-missing --cov=api tests/

'''
import pytest
from api.app import create_app
from api.database import db as _db
from api.config import TestConfig


@pytest.fixture(scope='function')
def app():
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    # Code after yield executes on teardown
    ctx.pop()

@pytest.fixture(scope='function')
def db(app):
    _db.app = app
    _db.create_all()
    yield _db
    # Code after yield executes on teardown
    _db.session.close()
    _db.drop_all()



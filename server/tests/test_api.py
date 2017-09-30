''' Tests for API '''
from flask import Flask
from flask_testing import TestCase
import unittest
import sys
sys.path.append('/src/api')
import models
'''

# import api
from models import db
'''

class ApiTestCase(TestCase):
    ''' Test case class for API '''
    def create_app(self):
        ''' Create Flask app for testing '''
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db/legocollector_test'
        app.config['SECRET_KEY'] = 'testing_key'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
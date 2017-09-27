'''
    Python/Flask REST API for Legocollector
'''
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_envvar('SETTINGS')
CORS(app)

# Views must be imported *after* creating Flask object
# (even though this violates pep8 rules)
# This also creates a circular dependency but should work ok
# See http://flask.pocoo.org/docs/0.12/patterns/packages/
import api.views  # nopep8

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

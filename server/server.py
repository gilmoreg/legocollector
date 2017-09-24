'''
    Python/Flask REST API for Legocollector
'''
from datetime import datetime as dt
from flask import Flask, jsonify, request, g

from flask_migrate import Migrate
import controller

app = Flask(__name__)
app.config.from_envvar('SETTINGS')

@app.route('/watches', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    return controller.get_all_watches()

@app.route('/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    # TOOD rip stuff off request
    return controller.add_watch()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

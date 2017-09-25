'''
    Python/Flask REST API for Legocollector
'''
from api import app
import api.controller as controller


@app.route('/watches', methods=['GET'])
def get_all_watches():
    ''' Return all watched sets '''
    return controller.get_all_watches()


@app.route('/add', methods=['POST'])
def add_watch():
    ''' Add a watched set to the database, return mongo ID '''
    # TOOD rip stuff off request
    return controller.add_watch()

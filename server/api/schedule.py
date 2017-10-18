''' 
/api/schedule.py 
Adapted from https://github.com/mrhwick/schedule/blob/master/schedule/__init__.py
'''
import datetime
import time
import threading
from api.controllers.legoset_controller import LegoSetController

next_call = time.time()


def update_stock_levels(app):
    ''' Task to update stock levels '''
    global next_call
    print('updating stock levels', datetime.datetime.now())
    with app.app_context():
        try:
            legoset_controller = LegoSetController()
            legoset_controller.update_stock_levels()
            print('stock levels updated', datetime.datetime.now())
        except:
            pass
        next_call = next_call+30 # seconds in an hour
        threading.Timer(next_call - time.time(), update_stock_levels).start()

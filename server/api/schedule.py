''' 
/api/schedule.py 
Adapted from https://github.com/mrhwick/schedule/blob/master/schedule/__init__.py
'''
import datetime
import threading
from api.controllers.legoset_controller import LegoSetController

def update_stock_levels(app):
    ''' Schedule update stock levels '''
    def job():
        ''' Task to run '''
        print('updating stock levels', datetime.datetime.now())
        with app.app_context():
            try:
                legoset_controller = LegoSetController()
                legoset_controller.update_stock_levels()
                print('stock levels updated', datetime.datetime.now())
            except Exception as e:
                print(e)
            # 3600 seconds in an hour
            threading.Timer(36000.0, job).start()

    # Start execution
    print('starting execution')
    job()

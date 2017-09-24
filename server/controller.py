'''
  Controller
'''
from models import Watch

def get_all_watches():
  ''' Return all Watches '''
  return Watch.query.all()

def add_watch(watch):
  ''' Add a new watch to the database '''
  new_watch = Watch(watch.set_id, watch.user)
  new_watch.save()
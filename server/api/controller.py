'''
  Controller
'''
from api.models import Watch

def get_all_watches():
  ''' Return all Watches '''
  # return Watch.query.all()
  return 'get_all_watches'

def add_watch(watch):
  ''' Add a new watch to the database '''
  # new_watch = Watch(watch.set_id, watch.user)
  # new_watch.save()
  return 'new_watch'
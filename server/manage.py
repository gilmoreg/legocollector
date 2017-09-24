from flask.ext.migrate import Migrate
from server import app, db

@app.cli.command()
def initdb():
  ''' Initialize the database '''
  migrate = Migrate(app, db)

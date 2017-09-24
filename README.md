# legocollector

## Installation
```
git clone https://github.com/gilmoreg/legocollector.git
cd legocollector
```
Create a 'config.py' file in server/ with the following content:
```
'''
  Settings for development
'''
DEBUG = True
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = '<secret>'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
```
Create a 'postgres.env' file in project root with the following content:
```
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=legocollector
```

Build and run Docker containers
```
docker-compose up
```

Create database migrations
```
# These steps may be unnecessary; they may have been originally necessary since the first time I created the container it did not have a proper config, which would not be true on a new machine
# The official postgres Docker image bakes a config into the container the first time it is created
# documenting my fix steps here for historical/future troubleshooting purposes
docker-compose exec db sh
/ # su postgres
/ $ pqsl
# For some reason SQLAlchemy/Alembic only wants to use the root role instead of the user I provided; this was my hack workaround (have have been due to above problem)
postgres=# CREATE ROLE root;
postgres=# ALTER ROLE root WITH LOGIN;
postgres=# ALTER ROLE root WITH Superuser;
# SQLAlchemy/Alembic wouldn't create the database either, only add tables to an existing one
postgres=# CREATE DATABASE legocollector;
postgres=# \q
/ $ exit
/ # exit

# Only the upgrade step (not db init or db migrate) will be necessary here if migrations were checked out from Git
docker-compose exec api sh
/ # cd src
/src # flask db init
/src # flask db migrate
/src # flask db upgrade 
```
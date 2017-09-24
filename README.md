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
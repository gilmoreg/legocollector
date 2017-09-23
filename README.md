# legocollector

## Installation
```
git clone https://github.com/gilmoreg/legocollector.git
cd legocollector
```
Create a 'settings.py' file in server/ with the following content:
```
'''
  Settings for development
'''
DEBUG = True
MONGO_URI = 'mongodb://<user>:<pass>@<host>:<port>/legotools'
```

Build and run Docker containers
```
docker-compose up
```
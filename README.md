# legocollector

by [Grayson Gilmore](https://github.com/gilmoreg/).

[See the live site here](http://gilmoreg.github.io/legocollector/).

## Screenshots
![lego collector screenshot](https://user-images.githubusercontent.com/18176333/32752876-a94dc512-c87f-11e7-857d-cbdc7c943bb7.png)

## Summary
People who collect Lego sets for profit want to know if stock is running out so they can rush to snap up one of the last remaining sets. Legocollector tracks stock levels on Amazon for Lego sets that you specify. Simply type in the set number and Legocollector will start tracking how many sets Amazon has for sale.

## Technical
* This is a full stack web app.
* The server is a Python/Flask app using Postgresql on Heroku.
  * Tests are run with pytest
  * [Bottlenose](https://github.com/lionheart/bottlenose) is used to interact with the Amazon Product Advertising API
  * BeautifulSoup parses the XML
  * Authentication is handled via JSON Web Tokens
  * Storage is a Heroku Postgresql database with SQLAlchemy as ORM
  * Development and deployment were done in Docker containers (rather than using virtualenv)
  * An AWS Lambda function runs every 6 hours to trigger an update of stock levels in the database. Using Celery was considered but proved impossible due to Heroku sleeping dynos.
* The client is a single page React/Redux app
  * This is an ejected Create React App project
  * [React-Chartjs-2](https://github.com/jerairrest/react-chartjs-2) renders the stock level charts

## Development Roadmap
* Possible features:
  * Email notification when stock levels fall below a user-defined threshold
  * Storing price information as well as stock levels
  * Other tools, such as comparing prices across sites, notifications of changes to the Lego Store deals page, and more...

## Installation
Docker Compose is used to run the database and server in development. You must have Docker installed to run this app locally. 
```
git clone https://github.com/gilmoreg/legocollector.git
cd legocollector
```
Create a 'server.env' file in server/ with the following content:
```
'''
  /server/server.env
  Settings for development
'''
FLASK_DEBUG=true
DATABASE_URL=postgresql://db/legocollector
AWS_ACCESS_KEY_ID=<access key id>
AWS_SECRET_ACCESS_KEY=<secret access key>
AWS_ASSOCIATE_TAG=<associate tag>
JWT_SECRET=<JWT signing secret>
ADMIN=<username for administrator>
```
Create a 'postgres.env' file in project root with the following content:
```
'''
  /postgres.env
  Settings for Postgresql Docker Container
'''
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
# Only the upgrade step (not db init or db migrate) will be necessary here if migrations were checked 
# out from Git
docker-compose exec api sh
/ # cd src
/src # flask db init
/src # flask db migrate
/src # flask db upgrade

# In production on Heroku, the migrations will already be in the container
# So this is all you need to do:
heroku run FLASK_APP=/src/migrate.py flask db upgrade
```

Build and start client:
```
cd client
npm install
npm start
```

### Serverless
Ensure Serverless Framework is installed (https://serverless.com/framework/docs/getting-started/)
Create a env.yml file in /serverless with the following content:
```
# /serverless/env.yml
ADMIN: <admin username>
SECRET: <JWT signing secret>
API_URL: <API url>
```
Deploy:
```
cd serverless
npm install
serverless deploy -v
```
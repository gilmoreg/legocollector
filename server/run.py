from api.app import create_app
from api.config import DevConfig

if __name__ == '__main__':
    flask_app = create_app(DevConfig)
    flask_app.run(host='0.0.0.0')

"""
Configuration class
"""
class Config():
    # TODO
    APP_NAME = 'Ragasa'

    # Enable debug mode
    DEBUG = True
    
    # TODO
    # Setup database URL and credentials
    # z o k e y
    # Not sure kung kelangan nyo to pero just keep it here for now
    APP_DB = {
        'host': 'localhost',
        'db': 'tubig',
        'user': 'root',
        'password': 'user',
        'port': 3306
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'.format(
        APP_DB['user'], APP_DB['password'], APP_DB['host'], APP_DB['db'])

    # Setup CORS
    ALLOWED_HEADERS = ['Origin', 'Accept', 'Content-Type', 'X-Requested-With', 'X-CSRF-Token']
    ALLOWED_ORIGINS = '*'
    ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

    # TODO
    # This is where frontend should go, create a route for all UI files
    # Setup template folder for webpages
    TEMPLATE_FOLDER = "templates"


    # TODO
    # Add nyo yung API key na makukuha nyo sa globe, pati ung app_id
    GLOBE_API_KEY = ""
    GLOBE_APP_ID = "pAoLsdr74jC7ocy9AjT7xyCd5AK8s9pq"

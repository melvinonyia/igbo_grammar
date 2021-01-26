from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()

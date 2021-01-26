from flask import Flask
from settings import config
from .extensions import db, migrate
from .api import api as api_blueprint

def create_app(config_name):
    """Application Factory - Create an instance of the Flask class and configure the Application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api.api_blueprint)

    return app

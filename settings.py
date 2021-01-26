"""
Configuration Settings
"""

import os

class Config:
    """Base configuration"""
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Development environment specific config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL')


class TestingConfig(Config):
    """Testing environment specific config"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    """Production environment specific config"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

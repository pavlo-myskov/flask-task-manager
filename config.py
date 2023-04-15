import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    '''live site accessed by final users'''
    ENV = "production"
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False


class StagingConfig(Config):
    '''preproduction environment used for previews and testing'''
    DEBUG = True
    DEVELOPMENT = False
    TESTING = False


class DevelopmentConfig(Config):
    '''local environment'''
    ENV = "development"
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True


def load_config():
    mode = os.getenv("ENV")
    if mode == "development":
        return DevelopmentConfig
    elif mode == "staging":
        return StagingConfig
    elif mode == "production":
        return ProductionConfig
    else:
        return Config

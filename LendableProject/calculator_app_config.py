
from dotenv import load_dotenv
import os
import secrets

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
dotflaskenv_path = os.path.join(APP_ROOT, '.flaskenv')


class BaseConfig:
    """Base config class"""
    SECRET_KEY = secrets.token_hex(20)
    DEBUG = True
    TESTING = False
    load_dotenv(dotenv_path)
    load_dotenv(dotflaskenv_path)


class ProductionConfig(BaseConfig):
    """Production specific config"""
    DEBUG = False


class StatingConfig(BaseConfig):
    """Staging specific config"""
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """Development environment specific config"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'not_really_secret?'

 
app_config = dict(
    production=ProductionConfig,
    development=DevelopmentConfig,
    staging=StatingConfig
)


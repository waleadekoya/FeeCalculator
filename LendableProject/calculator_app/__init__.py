from flask import Flask
from ..calculator_app_config import app_config
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    Bootstrap(app)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

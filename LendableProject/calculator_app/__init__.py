from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config['development'])

    return app

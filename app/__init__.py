from flask import Flask
from .api.v1 import version_1


def create_app():
	"""docstring for app's create_app method"""
    app = Flask(__name__)
    app.register_blueprint(version_1)
    return app

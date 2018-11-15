"""docstring for flask."""
from flask import Flask

from .api.v1 import version_1


def create_app():
    """Docstring for create_app method."""
    app = Flask(__name__)
    app.register_blueprint(version_1)
    return app

from flask import Flask, Blueprint
from .api.v1 import version_1

def create_app():
	app = Flask(__name__)
	app.register_blueprint(version_1)

	return app
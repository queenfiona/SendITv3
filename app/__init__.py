from flask import Api,Blueprint

def create_app():
	app= Flask(__name__)
	return app
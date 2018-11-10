from flask import Blueprint
from flask_restful import Api

version_1 = Blueprint('apiv1', __name__)
api = Api(version_1, prefix="/api/v1")

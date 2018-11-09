from flask import Blueprint
from flask_restful import Api, Resource
from .views.parcel_views import ParcelOrderView,SpecificParcelOrderView

version_1 = Blueprint('apiv1', __name__)

# Declare API and pass name of the Blueprint
api = Api(version_1, prefix="/api/v1")
api.add_resource(ParcelOrderView, "/parcels")
api.add_resource(SpecificParcelOrderView,"/parcels/<int:parcel_id>")
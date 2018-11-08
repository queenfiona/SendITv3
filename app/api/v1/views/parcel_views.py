from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, reqparse
from ..models.parcel_models import ParcelOrder


class ParcelOrderView(Resource, ParcelOrder):
    """docstring for ParcelOrderView"""

    def __init__(self):
        self.parcel = ParcelOrder()

    def post(self):
        data = request.get_json(force=True)
        user = data["user"]
        item_shipped = data["item_shipped"]
        origin = data["origin"]
        destination = data["destination"]
        weight = data["weight"]

        payload = self.parcel.create_parcel_delivery_order(
            user, item_shipped, origin, destination, weight)

        return make_response(jsonify(payload), 201)

    def get(self):
        parcel_delivery_orders = self.parcel.get_all_parcel_delivery_orders()
        payload = {
            "message": "success",
            "parcel orders": parcel_delivery_orders
        }
        return make_response(jsonify(payload), 200)

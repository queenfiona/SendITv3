"""docstring for flask import."""
from flask import jsonify, make_response, request

from flask_restful import Resource

from ..models.parcel_models import ParcelOrder


class ParcelOrderView(Resource, ParcelOrder):
    """docstring for ParcelOrderView."""

    def __init__(self):
        """Doctstring for ParcelOrderView init method."""
        self.parcel = ParcelOrder()

    def post(self):
        """Doctstring for ParcelOrderView post method."""
        data = request.get_json(force=True)
        user_id = data["user_id"]
        item_shipped = data["item_shipped"]
        origin = data["origin"]
        destination = data["destination"]
        weight = data["weight"]

        payload = self.parcel.create_parcel_delivery_order(
            user_id, item_shipped, origin, destination, weight)

        return make_response(jsonify(payload), 201)

    def get(self):
        """Doctstring for ParcelOrderView get method."""
        parcel_delivery_orders = self.parcel.get_all_parcel_delivery_orders()
        payload = {
            "message": "Order made",
            "parcel orders": parcel_delivery_orders
        }
        return make_response(jsonify(payload), 200)

        if not payload:
            not_found = {
                "message": "No order made yet"
            }
            return make_response(jsonify(not_found), 404)


class SpecificParcelOrderView(Resource, ParcelOrder):
    """docstring for SpecificParcelOrderView."""

    def __init__(self):
        """Doctstring for SpecificParcelOrderView init method."""
        self.parcel = ParcelOrder()

    def get(self, parcel_id):
        """Doctstring for SpecificParcelOrderView get method."""
        parcel_delivery_order = self.parcel.get_specific_order_by_id(
            parcel_id)
        payload = {
            "message": "success",
            "parcel order": parcel_delivery_order
        }
        return make_response(jsonify(payload), 200)

        if not parcel_delivery_order:
            """Doctstring for order not found."""
            return make_response(jsonify({"message": "Order not found"}), 404)


class UserSpecificParcelOrderView(Resource, ParcelOrder):
    """docstring for UserSpecificParcelOrderView."""

    def __init__(self):
        """Docstring for UserSpecificParcelOrderView init method."""
        self.parcel = ParcelOrder()

    def get(self, user_id):
        """Docstring for UserSpecificParcelOrderView get method."""
        user_parcel_orders = self.parcel.get_all_orders_by_specific_user(
            user_id)
        payload = {
            "message": "success",
            "parcel orders": user_parcel_orders
        }
        return make_response(jsonify(payload), 200)
        if not user_parcel_orders:
            """Doctstring for SpecificParcelOrderView init method."""
            payload = {
                "message": "User orders not found"
            }
            return make_response(jsonify(payload), 404)


class CancelSpecificParcelOrderView(Resource, ParcelOrder):
    """docstring for CancelSpecificParcelOrderView."""

    def __init__(self):
        """Docstring for CancelSpecificParcelOrderView init method."""
        self.parcel = ParcelOrder()

    def put(self, parcel_id):
        """Docstring for CancelSpecificParcelOrderView put method."""
        cancelled_delivery_order = self.parcel.cancel_specific_order(
            parcel_id)
        payload = {
            "message": "cancelled",
            "order": cancelled_delivery_order
        }
        return make_response(jsonify(payload), 200)
        if cancelled_delivery_order == "null":
            payload = {
                "message": "Order could not be cancelled"
            }
            return make_response(jsonify(payload), 404)

"""docstring for flask."""
from flask import Flask

from flask_restful import Api

app = Flask(__name__)
api = Api(app)

database = []


class ParcelOrder(object):
    """docstring for ParcelOrder."""

    def __init__(self):
        """Docstring for parcel models __init__."""
        self.database = database

    def create_parcel_delivery_order(self, user_id, item_shipped, origin, destination, weight, status="not_delivered"):
        """Docstring for create_parcel_delivery_order method."""
        payload = {
            "parcel_id": len(self.database) + 1,
            "user_id": int(user_id),
            "item_shipped": item_shipped,
            "origin": origin,
            "destination": destination,
            "weight": int(weight),
            "status": status
        }

        self.database.append(payload)
        return payload

    def get_all_parcel_delivery_orders(self):
        """Docstring for get_all_parcel_delivery_orders method."""
        return self.database

    def get_specific_order_by_id(self, parcel_id):
        """Docstring for get_specific_order_by_id method."""
        for order in self.database:
            if order["parcel_id"] == int(parcel_id):
                return order

    def get_all_orders_by_specific_user(self, user_id):
        """Docstring for get_all_orders_by_specific_user method."""
        orders = []
        for order in self.database:
            if order["user_id"] == int(user_id):
                orders.append(order)
            return orders

    def cancel_specific_order(self, parcel_id, status):
        """Docstring for cancel_specific_order method."""
        for order in self.database:
            if order["parcel_id"] == parcel_id:
                if order["status"] == "not_delivered":
                    order["status"] = "cancel"
                    order["user_id"] = order["user_id"]
                    order["item_shipped"] = order["item_shipped"]
                    order["origin"] = order["origin"]
                    order["destination"] = order["destination"]
                    order["weight"] = order["weight"]

                    index = next(index for index, order in enumerate(
                        self.database) if order["parcel_id"] == parcel_id)
                    # Remove existing order to be cancelled
                    self.database.remove(self.database[index])
                    # Replace the order with the cancelled order
                    self.database.insert(index, order)

                    return order

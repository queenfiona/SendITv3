from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

database = []


class ParcelOrder(object):
    """docstring for ParcelOrder"""

    def __init__(self):
        self.database = database

    def create_parcel_delivery_order(self, user, item_shipped, origin, destination, weight, status="not_delivered"):
        payload = {
            "parcel_id": len(self.database) + 1,
            "user": user,
            "item_shipped": item_shipped,
            "origin": origin,
            "destination": destination,
            "weight": int(weight),
            "status": status
        }

        self.database.append(payload)
        return payload

    def get_all_parcel_delivery_orders(self):
        return self.database

    def get_specific_order_by_id(self, parcel_id):
        for order in self.database:
            if order["parcel_id"] == int(parcel_id):
                payload = {
                    "message": "success",
                    "parcel_order": order
                }
                return payload

    def get_all_orders_by_specific_user(self, user):
        orders = []
        for order in self.database:
            if order["user"] == str(user):
                orders.append(order)
                payload = {
                    "message": "success",
                    "parcel_order": orders
                }
            return payload

    def cancel_specific_order(self, parcel_id, status):
        for order in self.database:
            if order["parcel_id"] == parcel_id and order["status"] == "not_delivered":
                order["status"] = status
                order["user"] = order["user"]
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

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

database = []


class ParcelOrder(object):
    def __init__(self):
        self.database = database

    def create_parcel_delivery_order(self, user, item_shipped, origin, destination, weight, status="Not delivered"):
        payload = {
            "parcel_id": len(self.database) + 1,
            "user": user,
            "item_shipped": item_shipped,
            "origin": origin,
            "destination": destination,
            "weight": weight,
            "status": status
        }

        self.database.append(payload)
        return payload

    def get_all_parcel_delivery_orders(self):
        return self.database
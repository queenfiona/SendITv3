import unittest
import json
from flask import Flask
from app import create_app


class TestCase(unittest.TestCase):
    """docstring for TestCase"""

    def setUp(self):
        app = create_app()
        self.client = app.test_client()
        self.data={
            "user":"queenfiona",
            "parcel_id": 1,
            "item_shipped":"Books",
            "origin":"Nairobi",
            "destination": "Mombasa",
            "weight":5,
            "status":"not_delivered"
        }

    def tearDown(self):
        pass

    def test_post_parcels(self):
        res = self.client.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
    unittest.main()

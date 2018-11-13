"""docstring for unittest import."""
import unittest
import json
from app import create_app


class TestCase(unittest.TestCase):
    """docstring for TestCase."""

    def setUp(self):
        """Docstring for setUp method."""
        app = create_app()
        self.client = app.test_client()
        self.data = {
            "user_id": 1,
            "parcel_id": 1,
            "item_shipped": "Books",
            "origin": "Nairobi",
            "destination": "Mombasa",
            "weight": 5,
            "status": "not_delivered"
        }
        self.c = 'application/json'

    def tearDown(self):
        """Docstring for tearDown method."""
        pass

    def test_post_parcels_api(self):
        """Docstring for setUp method."""
        res = self.client.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type=self.c)
        self.assertEqual(res.status_code, 201)

    def test_get_all_parcels_api(self):
        """Docstring for setUp method."""
        res = self.client.get(
            '/api/v1/parcels', data=json.dumps(self.data), content_type=self.c)
        result = json.loads(res.data)
        self.assertEqual(result["message"], "success")
        self.assertEqual(res.status_code, 200)

    def test_get_by_id_api(self):
        """Docstring for setUp method."""
        c = "application/json"
        res = self.client.get(
            '/api/v1/parcels/1', data=json.dumps(self.data), content_type=c)
        result = json.loads(res.data)
        self.assertEqual(result["message"], "success")
        self.assertEqual(res.status_code, 200)

    def test_get_by_user_id_api(self):
        """Docstring for setUp method."""
        res = self.client.get(
            '/api/v1/users/1/parcels', data=json.dumps(self.data), content_type=self.c)
        result = json.loads(res.data)
        self.assertEqual(result["message"], "success")
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()


from app import flask_app
import unittest
import os
MONGODB_USERNAME = os.environ["MONGODB_USERNAME"]
MONGODB_PASSWORD = os.environ["MONGODB_PASSWORD"]
from pymongo import MongoClient
client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.26bu2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db
products = db.products

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client() # Sets up the test client, a test app for us to use.
        self.app.testing = True

    # Test 1: Route Test
    def test_route(self):
        response = self.app.post("/index") # Populate "response" with what we get when we post to /index.
        self.assertEqual(response.status_code, 405) # Assert the response.status code is 405, otherwise fail.

    def test_read_operation(self):
        response = client.db_name.command('ping') # Populate response with what we get back from pinging the database with this command.
        self.assertEqual(response, {u'ok': 1.0}) # Assert the response is equal to MongoDB's okay signal, otherwise fail.

    def test_write_data_to_db(db):
        new_data = {"field": "new_value"} # Create sample data.
        products.insert_one(new_data) # Insert the sample data into our products collection.
        inserted_data = products.find_one({"field": "new_value"}) # Set inserted data to our sample data if we find it in our database, verifying it was inserted.
        assert inserted_data is not None # Assert that inserted_data isn't empty.
        assert inserted_data['field'] == 'new_value' # Assert that the inserted_data is indeed our sample data.
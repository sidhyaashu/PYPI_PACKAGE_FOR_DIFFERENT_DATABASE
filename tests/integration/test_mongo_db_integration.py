# tests/integration/test_mongo_db_integration.py

import pytest
from src.MultiDBConnector.mongo_db import MongoDBConnector

@pytest.fixture(scope='module')
def mongo_connector():
    uri = 'mongodb://localhost:27017'  # Update with your test MongoDB URI
    connector = MongoDBConnector(uri)
    connector.connect()
    yield connector
    connector.close()

def test_mongo_db_integration(mongo_connector):
    db = mongo_connector.client.test_db
    collection = db.test_collection

    # Insert a document
    result = collection.insert_one({"name": "test", "value": 123})
    assert result.inserted_id is not None

    # Query the document
    document = collection.find_one({"name": "test"})
    assert document is not None
    assert document['value'] == 123

    # Clean up
    collection.delete_one({"name": "test"})

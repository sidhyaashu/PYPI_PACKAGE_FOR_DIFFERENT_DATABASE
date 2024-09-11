# tests/unit/test_mongo_db_unit.py

import pytest
from src.MultiDBConnector.mongo_db import MongoDBConnector

@pytest.fixture
def mongo_connector():
    return MongoDBConnector(uri="mongodb://localhost:27017")

def test_connect(mongo_connector):
    client = mongo_connector.connect()
    assert client is not None

def test_close(mongo_connector):
    mongo_connector.connect()
    mongo_connector.close()
    # No direct way to verify closure, but no exceptions should be thrown

# tests/integration/test_pinecone_db_integration.py

import pytest
import pinecone
from src.MultiDBConnector.pinecone_db import PineconeDBConnector

@pytest.fixture(scope='module')
def pinecone_connector():
    connector = PineconeDBConnector(api_key='test-api-key')
    connector.connect()
    yield connector
    connector.close()

def test_pinecone_db_integration(pinecone_connector):
    index_name = "test-index"

    # Create an index
    pinecone.create_index(name=index_name, dimension=128)
    
    # Add a vector
    pinecone_index = pinecone.Index(index_name)
    pinecone_index.upsert(vectors=[("id1", [0.1] * 128)])

    # Query the vector
    results = pinecone_index.query(ids=["id1"])
    assert len(results.matches) > 0
    assert results.matches[0].id == "id1"

    # Clean up
    pinecone.delete_index(index_name)

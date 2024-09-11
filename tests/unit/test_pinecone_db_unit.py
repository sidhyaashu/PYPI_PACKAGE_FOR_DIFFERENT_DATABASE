# tests/unit/test_pinecone_db_unit.py

import pytest
from unittest.mock import patch
from src.MultiDBConnector.pinecone_db import PineconeDBConnector

@pytest.fixture
def pinecone_connector():
    return PineconeDBConnector(api_key="test-api-key")

@patch('pinecone.init')
@patch('pinecone.Client')
def test_connect(mock_client, mock_init, pinecone_connector):
    # Mock the Pinecone client object
    mock_client.return_value = 'Mock Pinecone Client'
    
    # Call the connect method
    client = pinecone_connector.connect()
    
    # Assert that the client is properly returned
    assert client == 'Mock Pinecone Client'
    
    # Ensure pinecone.init was called with the correct API key
    mock_init.assert_called_with(api_key="test-api-key")

def test_close(pinecone_connector):
    # The close method does nothing in this case, but we can still test for absence of errors
    try:
        pinecone_connector.close()
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

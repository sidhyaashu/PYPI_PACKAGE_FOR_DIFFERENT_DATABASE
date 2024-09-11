# tests/unit/test_postgresql_db_unit.py

import pytest
from src.MultiDBConnector.postgresql_db import PostgreSQLDBConnector

@pytest.fixture
def postgres_connector():
    return PostgreSQLDBConnector(user="user", password="password", host="localhost", database="testdb")

def test_connect(postgres_connector):
    connection = postgres_connector.connect()
    assert connection is not None

def test_close(postgres_connector):
    postgres_connector.connect()
    postgres_connector.close()
    # No direct way to verify closure, but no exceptions should be thrown

# tests/unit/test_mysql_db_unit.py

import pytest
from src.MultiDBConnector.mysql_db import MySQLDBConnector

@pytest.fixture
def mysql_connector():
    return MySQLDBConnector(user="user", password="password", host="localhost", database="testdb")

def test_connect(mysql_connector):
    connection = mysql_connector.connect()
    assert connection is not None

def test_close(mysql_connector):
    mysql_connector.connect()
    mysql_connector.close()
    # No direct way to verify closure, but no exceptions should be thrown

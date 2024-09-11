# tests/integration/test_mysql_db_integration.py

import pytest
import mysql.connector
from src.MultiDBConnector.mysql_db import MySQLDBConnector

@pytest.fixture(scope='module')
def mysql_connector():
    connector = MySQLDBConnector(
        user='test_user',
        password='test_password',
        host='localhost',
        database='test_db'
    )
    connector.connect()
    yield connector
    connector.close()

def test_mysql_db_integration(mysql_connector):
    cursor = mysql_connector.connection.cursor()
    
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            value INT
        )
    """)
    
    # Insert a row
    cursor.execute("INSERT INTO test_table (name, value) VALUES (%s, %s)", ('test', 123))
    mysql_connector.connection.commit()

    # Query the row
    cursor.execute("SELECT * FROM test_table WHERE name = %s", ('test',))
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == 'test'
    assert row[2] == 123

    # Clean up
    cursor.execute("DROP TABLE test_table")
    mysql_connector.connection.commit()
    cursor.close()

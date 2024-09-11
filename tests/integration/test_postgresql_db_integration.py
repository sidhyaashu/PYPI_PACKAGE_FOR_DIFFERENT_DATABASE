# tests/integration/test_postgresql_db_integration.py

import pytest
import psycopg2
from src.MultiDBConnector.postgresql_db import PostgreSQLDBConnector

@pytest.fixture(scope='module')
def postgres_connector():
    connector = PostgreSQLDBConnector(
        user='test_user',
        password='test_password',
        host='localhost',
        database='test_db'
    )
    connector.connect()
    yield connector
    connector.close()

def test_postgresql_db_integration(postgres_connector):
    cursor = postgres_connector.connection.cursor()
    
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            value INTEGER
        )
    """)
    
    # Insert a row
    cursor.execute("INSERT INTO test_table (name, value) VALUES (%s, %s)", ('test', 123))
    postgres_connector.connection.commit()

    # Query the row
    cursor.execute("SELECT * FROM test_table WHERE name = %s", ('test',))
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == 'test'
    assert row[2] == 123

    # Clean up
    cursor.execute("DROP TABLE test_table")
    postgres_connector.connection.commit()
    cursor.close()

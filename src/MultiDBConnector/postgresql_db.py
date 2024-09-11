# src/MultiDBConnector/postgresql_db.py

import psycopg2
from .core_db import CoreDBConnector

class PostgreSQLDBConnector(CoreDBConnector):
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
    
    def connect(self):
        self.connection = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        return self.connection
    
    def close(self):
        if self.connection:
            self.connection.close()

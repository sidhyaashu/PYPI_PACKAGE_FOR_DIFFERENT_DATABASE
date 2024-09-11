# src/MultiDBConnector/mysql_db.py

import mysql.connector
from .core_db import CoreDBConnector

class MySQLDBConnector(CoreDBConnector):
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
    
    def connect(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        return self.connection
    
    def close(self):
        if self.connection:
            self.connection.close()

# src/MultiDBConnector/mongo_db.py

from pymongo import MongoClient
from .core_db import CoreDBConnector

class MongoDBConnector(CoreDBConnector):
    def __init__(self, uri):
        self.uri = uri
        self.client = None
    
    def connect(self):
        self.client = MongoClient(self.uri)
        return self.client
    
    def close(self):
        if self.client:
            self.client.close()

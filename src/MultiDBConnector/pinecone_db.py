# src/MultiDBConnector/pinecone_db.py

import pinecone
from .core_db import CoreDBConnector

class PineconeDBConnector(CoreDBConnector):
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = None
    
    def connect(self):
        pinecone.init(api_key=self.api_key)
        self.client = pinecone.Client()
        return self.client
    
    def close(self):
        # Pinecone doesn't have a close method, but you might manage resources here
        pass

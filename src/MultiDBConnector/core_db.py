# src/MultiDBConnector/core_db.py

class CoreDBConnector:
    def connect(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def close(self):
        raise NotImplementedError("Subclasses should implement this!")

# tests/unit/test_core_unit.py

import pytest
from src.MultiDBConnector.core_db import CoreDBConnector

class MockDBConnector(CoreDBConnector):
    def connect(self):
        return "Mock Connection"
    
    def close(self):
        return "Mock Closed"

def test_connect():
    db = MockDBConnector()
    assert db.connect() == "Mock Connection"

def test_close():
    db = MockDBConnector()
    assert db.close() == "Mock Closed"

# src/MultiDBConnector/utils.py

def get_db_connector(db_type, **kwargs):
    from .mongo_db import MongoDBConnector
    from .mysql_db import MySQLDBConnector
    from .postgresql_db import PostgreSQLDBConnector
    from .pinecone_db import PineconeDBConnector
    
    connectors = {
        'mongodb': MongoDBConnector,
        'mysql': MySQLDBConnector,
        'postgresql': PostgreSQLDBConnector,
        'pinecone': PineconeDBConnector,
    }
    
    if db_type not in connectors:
        raise ValueError(f"Unsupported database type: {db_type}")
    
    return connectors[db_type](**kwargs)

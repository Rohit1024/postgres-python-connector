import os
from typing import Generator

from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import sqlalchemy
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

# Global connection pool
pool = None 
ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

def connect_with_connector() -> Engine:
    """
    Establishes a connection to Google Cloud SQL using the Cloud SQL Connector.
    
    Returns:
        sqlalchemy.engine.base.Engine: A SQLAlchemy engine for database connections
    """
    instance_connection_name = os.environ.get("INSTANCE_CONNECTION_NAME", "")
    db_user = os.environ.get("DB_USER", "")
    db_name = os.environ.get("DB_NAME", "")

    if not all([instance_connection_name, db_user, db_name]):
        raise ValueError("Missing required database connection environment variables")

    # Initialize the connector
    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        """
        Creates a database connection using the Cloud SQL Connector.
        
        Returns:
            pg8000.dbapi.Connection: A database connection
        """
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            db=db_name,
            ip_type=ip_type,
            enable_iam_auth=True,
        )
        return conn

    # Create the connection pool
    engine = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn
    )
    return engine

def get_db_connection() -> Generator[Session, None, None]:
    """
    Creates a database connection generator for use in dependency injection.
    
    Yields:
        sqlalchemy.orm.Session: A database session
    """
    global pool
    if pool is None:
        pool = connect_with_connector()
    
    with pool.connect() as connection:
        try:
            yield connection
        finally:
            connection.close()

def get_IP_TYPE() :
    return f"Hello from Cloud SQL:Postgres Python Connector : {ip_type} IP Demo"
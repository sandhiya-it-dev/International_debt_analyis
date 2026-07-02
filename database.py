import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

# Locate and ingest core structural database environment variables
load_dotenv()

@st.cache_resource
def get_engine():
    """
    Initializes and caches an enterprise-grade SQLAlchemy engine instance.
    Uses connection pooling to prevent connection overhead on application re-runs.
    """
    # Pull discrete parameters out of system memory
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD", "")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "postgres")
    
    # Construct a valid, production-ready PostgreSQL connection URI string
    connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    # Instantiate the cached connection engine with a pool size optimized for web frames
    engine = create_engine(
        connection_string,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True # Checks if connection is alive before routing queries
    )
    
    return engine
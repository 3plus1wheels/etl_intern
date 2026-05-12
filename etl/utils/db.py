import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_database_url() -> str:
    load_dotenv()
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB", "vehicle_analytics")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"


def get_engine() -> Engine:
    return create_engine(get_database_url(), pool_pre_ping=True)

import databases
from sqlalchemy import MetaData, create_engine
from src.config import settings



database = databases.Database(settings.database_url)
metadata =  MetaData()

if settings.environment == "production":
    engine = create_engine(settings.database_url)
else:
    engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
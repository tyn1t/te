from src.database import metadata 

from sqlalchemy import Table ,Column, Integer, Numeric, TIMESTAMP, func


accounts = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False, index=True),
    Column("balance", Numeric(10, 0), default=0),
    Column("created_at", TIMESTAMP(timezone=True), default=func.now()),
)

import enum
from sqlalchemy import Table, Column, Integer, Numeric, Enum, func, ForeignKey, TIMESTAMP
from src.database import metadata

class TransactionType(str, enum.Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    

transactions = Table(
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("accounts_id", Integer, ForeignKey("accounts.id"), nullable=False),
    Column("type", Enum(TransactionType, name="transaction_types"), nullable=False),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("timestamp", TIMESTAMP(timezone=True), default=func.now()),
)
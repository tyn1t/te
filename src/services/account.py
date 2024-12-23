from databases.interfaces import Record

from src.models.account import accounts 
from src.database import database
from src.schemas.account import AccountIn 


class AccountServer():
    
    
    async def real_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = accounts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)
    
    
    async def create(self, account: AccountIn) -> Record:
        command = accounts.insert().values(user_id=account.user_id, balance=account.balance)
        account_id = await database.execute(command)

        query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(query)
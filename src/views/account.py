from pydantic import BaseModel, AwareDatetime, NaiveDatetime, PositiveFloat 


class AccountOut(BaseModel):
    id: int  
    user_id: int 
    balance: float 
    created_at: AwareDatetime | NaiveDatetime 


class TransactionOut(BaseModel): 
    id: int  
    accounts_id: int 
    type : str
    amount: PositiveFloat 
    timestamp: AwareDatetime | NaiveDatetime

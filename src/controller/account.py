from fastapi import APIRouter, status

from src.schemas.account import AccountIn
from src.services.account import AccountServer
from src.views.account import AccountOut, TransactionOut
from src.services.transaction import TransactionService

# from src.security import login_required

router = APIRouter(prefix="/accounts")

account_server = AccountServer()
tx_service = TransactionService()

@router.get("/", response_model=list[AccountOut])
async def real_all(limit: int, skip: int):
    return await account_server.real_all(limit=limit, skip=skip)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_accounts(account: AccountIn):
    return await account_server.create(account)

@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0):
    return await tx_service.read_all(account_id=id, limit=limit, skip=skip)


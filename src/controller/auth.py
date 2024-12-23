from fastapi import APIRouter

from src.views.auth import LoginOut 
from src.schemas.auth import LoginIn 
from src.security import sign_jwt


router = APIRouter(prefix="/auth")

@router.post("/ligin", response_model=LoginOut)
async def login(data: LoginIn):
    return await sign_jwt(user_id=data.user_id)
from contextlib import asynccontextmanager


from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.database import database

from src.controller import account
from src.controller import transaction 
from src.controller import auth
from src.exceptions import AccountNotFoundError, BusinessError



@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()
    
app = FastAPI(
    title="Transactions API",
    version="1.0.0",
    lifespan=lifespan,
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(account.router, tags=["accounts"])
app.include_router(transaction.router, tags=["transaction"])
app.include_router(auth.router, tags=["login"])


@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(request: Request, exc: AccountNotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Account not found."})


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})
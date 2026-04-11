from fastapi import APIRouter

from core.schemas.create_account_response_schema import CreateAccountResponseSchema
from core.schemas.login_response_schema import LoginResponseSchema
from dtos.create_account_dto import CreateAccountDTO
from dtos.login_dto import LoginDTO
from services.account_service import AccountService

router = APIRouter()

service = AccountService()


@router.post("/auth/login", response_model=LoginResponseSchema)
def login(login_dto: LoginDTO):
    return service.login(login_dto)


@router.post("/account", response_model=CreateAccountResponseSchema)
def create_account(create_account_dto: CreateAccountDTO):
    return service.create_account(create_account_dto)


@router.get("/account/{cpf}")
def get_account(cpf: str):
    return service.get_account_by_cpf(cpf)

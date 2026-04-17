from fastapi import APIRouter

from core.schemas.responses.create_account_response_schema import CreateAccountResponseSchema
from dtos.create_account_dto import CreateAccountDTO
from services.account_service import AccountService
from models.user import User
router = APIRouter()

service = AccountService()


@router.post("/user", response_model=CreateAccountResponseSchema)
def create_account(account: CreateAccountDTO):
    account_validation = User
    return service.create_account(account)

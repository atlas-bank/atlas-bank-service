from fastapi import APIRouter

from core.schemas.responses.account_validation_response_schema import AccountValidationResponseSchema
from core.schemas.responses.create_user_response_schema import CreateAccountResponseSchema
from core.schemas.responses.login_response_schema import LoginResponseSchema
from dtos.create_user_dto import CreateAccountDTO
from dtos.login_dto import LoginDTO, ValidateAccountDTO
from services.account_service import AccountService
from models.user import User
router = APIRouter()

service = AccountService()


@router.post("/auth/login", response_model=LoginResponseSchema)
def login(login_dto: LoginDTO):
    return service.login(login_dto)


@router.post("/auth/validate", response_model=AccountValidationResponseSchema)
def validate_account(validate_account_dto: ValidateAccountDTO):
    return service.validate_account(validate_account_dto)

@router.get("/account/{cpf}")
def get_account(cpf: str):
    return service.get_account_by_cpf(cpf)

from fastapi import APIRouter

from core.schemas.responses.create_user_response_schema import CreateUserResponseSchema
from dtos.create_user_dto import CreateUserDTO
from services.user_service import UserService
from repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/user", response_model=CreateUserResponseSchema)
def create_account(user: CreateUserDTO):
    repo = UserRepository()
    service = UserService(repo)

    return service.create_user(user)

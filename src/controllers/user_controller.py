from fastapi import APIRouter

from core.schemas.responses.create_user_response_schema import CreateUserResponseSchema
from dtos.create_user_dto import CreateUserDTO
from services.user_service import UserService
from models.user import User

router = APIRouter()

service = UserService()


@router.post("/user", response_model=CreateUserResponseSchema)
def create_account(user: CreateUserDTO):
    return service.create_user(user)

from pydantic import BaseModel
from models.user import User

class CreateUserDTO(BaseModel):
    user: User
    password: str

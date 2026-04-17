from pydantic import BaseModel
from models.user import User

class CreateAccountDTO(BaseModel):
    user: User
    password: str

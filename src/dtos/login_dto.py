from pydantic import BaseModel


class LoginDTO(BaseModel):
    agency:str
    account: str
    password: str

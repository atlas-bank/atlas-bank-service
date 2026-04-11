from pydantic import BaseModel


class LoginDTO(BaseModel):
    agency:str
    account_number: str
    password: str

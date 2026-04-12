from pydantic import BaseModel


class LoginDTO(BaseModel):
    branch: str
    account_number: str
    cpf: str
    password: str


class ValidateAccountDTO(BaseModel):
    branch: str
    account_number: str

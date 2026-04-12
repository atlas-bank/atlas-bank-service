from pydantic import BaseModel


class LoginDTO(BaseModel):
    validate_token: str
    password: str


class ValidateAccountDTO(BaseModel):
    branch: str
    account_number: str

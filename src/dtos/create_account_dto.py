from pydantic import BaseModel


class CreateAccountDTO(BaseModel):
    cpf: str
    password: str

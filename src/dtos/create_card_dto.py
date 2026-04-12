from pydantic import BaseModel


class CreateCardDTO(BaseModel):
    cpf: str
    pin: str
    userFullName: str
    deviceId: str
    brand: str
    international: bool

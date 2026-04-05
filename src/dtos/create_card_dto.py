from pydantic import BaseModel


class CreateCardDTO(BaseModel):
    userCPF: str
    pin: str
    userFullName: str
    deviceId: str
    brand: str
    international: bool

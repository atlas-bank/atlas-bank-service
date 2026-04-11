from pydantic import BaseModel


class LoginResponseSchema(BaseModel):
    message: str = "Login successful"

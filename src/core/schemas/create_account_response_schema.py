from pydantic import BaseModel


class CreateAccountResponseSchema(BaseModel):
    message: str = "Account created successfully"
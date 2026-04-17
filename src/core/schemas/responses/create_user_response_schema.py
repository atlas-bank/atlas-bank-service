from pydantic import BaseModel


class CreateUserResponseSchema(BaseModel):
    message: str = "User created successfully"
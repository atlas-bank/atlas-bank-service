from pydantic import BaseModel


class AccountValidationResponseSchema(BaseModel):
    message: str = "Successfully validated account_number, please proceed to login"
    data: dict = {
        "validate_token": "UUID"
    }

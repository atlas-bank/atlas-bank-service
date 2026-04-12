from exceptions.exceptions import BadRequestException
from interfaces.entities_interface import IEntity


class Account(IEntity):
    @classmethod
    def get_collection(cls) -> str:
        return "accounts"

    def __init__(self, branch, account_number, cpf, password=None):
        self.branch = branch
        self.account_number = account_number
        self.password = password
        self.cpf = cpf

    def to_dict(self):
        return self.__dict__

    def validate_and_set_password(self, password: str):
        if not len(password) == 6:
            raise BadRequestException("Invalid password length")
        elif not password.isdigit():
            raise BadRequestException("Password must contain only digits")
        self.password = password

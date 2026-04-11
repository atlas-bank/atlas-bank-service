from exceptions.exceptions import BadRequestException
from interfaces.entities_interface import IEntity


class Account(IEntity):
    @classmethod
    def get_collection(cls) -> str:
        return "account"

    def __init__(self, agency, account, user_cpf, password=None):
        self.agency = agency
        self.account = account
        self.password = password
        self.user_cpf = user_cpf

    def to_dict(self):

        return self.__dict__

    def validate_and_set_password(self, password: str):
        if not len(password) == 6:
            raise BadRequestException("Invalid password length")
        elif not password.isdigit():
            raise BadRequestException("Password must contain only digits")
        self.password = password

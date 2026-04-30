from exceptions.exceptions import BadRequestException
from interfaces.entities_interface import IEntity
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

class Account(IEntity):
    @classmethod
    def get_collection(cls) -> str:
        return "accounts"

    _ph = PasswordHasher()

    def __init__(self, branch, account_number, cpf, password=None,
                 validate_token=None,
                 validate_token_expiration=None,
                 login_attempt=None,
                 is_blocked=None):
        self.branch = branch
        self.account_number = account_number
        self.password = password
        self.cpf = cpf
        self.validate_token = validate_token
        self.validate_token_expiration = validate_token_expiration
        self.login_attempt = login_attempt or 0
        self.is_blocked: bool = is_blocked

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def validate_password(self, password: str):
        if len(password) != 6:
            raise BadRequestException("Invalid password length")
        elif not password.isdigit():
            raise BadRequestException("Password must contain only digits")

    @staticmethod
    def set_password(self, password: str):
        self.validate_password(password)
        self.password = self._ph.hash(password)


def verify_password(self, password: str) -> bool:
    try:
        return self._ph.verify(self.password, password)
    except (VerifyMismatchError, VerificationError):
        return False
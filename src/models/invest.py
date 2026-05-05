from interfaces.entities_interface import IEntity
from models.account import Account
from models.user import User


class Invest(IEntity):
    @classmethod
    def get_collection(cls) -> str:
        return "invests"

    def __init__(self, account:Account,user:User):
        self.cpf = account.cpf
        self.account_number = account.account_number
        self.name = user.full_name
        self.email = user.email


    def to_dict(self):
        return self.__dict__


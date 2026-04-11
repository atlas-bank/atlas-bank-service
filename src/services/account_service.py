import random
from http import HTTPStatus

from dtos.create_account_dto import CreateAccountDTO
from exceptions.exceptions import UnauthorizedException
from models.account import Account
from repositories.account_repository import AccountRepository
from services.api_response import api_response

class AccountService:
    def __init__(self):
        self.repository = AccountRepository()
        self.agencies = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]

    def create_account(self, create_account_dto: CreateAccountDTO):
        account_number = self.generate_account_number()
        dv = self.calculate_dv(account_number)
        account = Account(agency=str(self.select_random_agency()), account=str(account_number) + str(dv),
                          user_cpf=create_account_dto.cpf)

        account.validate_and_set_password(create_account_dto.password)
        print(account.to_dict())
        self.repository.save(account)
        return api_response(
            status_code=HTTPStatus.CREATED,
            message="Account created successfully",
        )
    def get_account_by_cpf(self, cpf: str):
        return self.repository.find_by_cpf(cpf).to_dict()

    def select_random_agency(self):
        agency_idx = random.randint(0, len(self.agencies) - 1)
        return self.agencies[agency_idx]

    @staticmethod
    def generate_account_number():
        return random.randint(100000000, 999999999)

    @staticmethod
    def calculate_dv(account_number):
        return (account_number - 1) % 9 + 1

    def login(self, login_dto):
        account = self.repository.find_by_login_credentials(login_dto)
        print(account)
        if not account or account.password != login_dto.password:
            if account:
                # incrementa tentativa de login
                pass
            raise UnauthorizedException("Please check your login details and try again.")

        return api_response(
            status_code=HTTPStatus.OK,
            message="Login successful",
        )

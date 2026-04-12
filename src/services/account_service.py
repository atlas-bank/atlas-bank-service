import random
from http import HTTPStatus

from dtos.create_account_dto import CreateAccountDTO
from dtos.login_dto import ValidateAccountDTO
from exceptions.exceptions import UnauthorizedException
from models.account import Account
from repositories.account_repository import AccountRepository
from services.api_response import api_response


class AccountService:
    def __init__(self):
        self.repository = AccountRepository()
        self.branches = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]

    def create_account(self, create_account_dto: CreateAccountDTO):
        account_number = self.generate_account_number()
        check_digit = self.calculate_check_digit(account_number)
        account = Account(branch=str(self.select_random_branch()),
                          account_number=str(account_number) + str(check_digit), cpf=create_account_dto.cpf)

        account.validate_and_set_password(create_account_dto.password)
        print(account.to_dict())
        self.repository.save(account)
        return api_response(
            status_code=HTTPStatus.CREATED,
            message="Account created successfully",
        )

    def get_account_by_cpf(self, cpf: str):
        return api_response(
            status_code=HTTPStatus.OK,
            message="Account found successfully",
            data=self.repository.find_by_cpf(cpf).to_dict()
        )

    def select_random_branch(self):
        branch_idx = random.randint(0, len(self.branches) - 1)
        return self.branches[branch_idx]

    @staticmethod
    def generate_account_number():
        return random.randint(100000000, 999999999)

    @staticmethod
    def calculate_check_digit(account_number):
        return (account_number - 1) % 9 + 1

    def login(self, login_dto):
        account = self.repository.find_by_login_credentials(login_dto)
        if not account or account.password != login_dto.password:
            if account:
                # incrementa tentativa de login
                pass
            raise UnauthorizedException("Please check your login details and try again.")

        return api_response(
            status_code=HTTPStatus.OK,
            message="Login successful",
        )

    def validate_account(self, validate_account_dto: ValidateAccountDTO):
        is_digit_valid = self.validate_check_digit(validate_account_dto.account_number)
        account_exists = self.repository.exists_by_account(account=validate_account_dto)

        if not is_digit_valid or not account_exists:
            raise UnauthorizedException("Please check your login details and try again.")

        return api_response(
            status_code=HTTPStatus.OK,
            message="Successfully validated account_number, please proceed to login",
        )

    def validate_check_digit(self, account_number: str):
        account_number_no_cd = int(account_number[:-1])  # remove o ultimo char
        check_digit = int(account_number[-1])  # pega o ultimo char
        calculated_check_digit = self.calculate_check_digit(account_number_no_cd)
        return calculated_check_digit == check_digit

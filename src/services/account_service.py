import logging
import random
from datetime import datetime, timedelta, timezone
from http import HTTPStatus

from dtos.create_account_dto import CreateAccountDTO
from dtos.login_dto import ValidateAccountDTO, LoginDTO
from exceptions.exceptions import UnauthorizedException
from models.account import Account
from repositories.account_repository import AccountRepository
from services.api_response import api_response
from utils.token_generator import generate_random_token

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


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

    def validate_password(self, account: Account, provided_password: str):
        print(account.to_dict())
        if account.is_blocked:
            raise UnauthorizedException("Your account is blocked due to excessive login attempts.")

        if account.password != provided_password:
            self.repository.increase_invalid_login_chance(validate_token=account.validate_token, max_attempts=5)
            raise UnauthorizedException("Please check your login details and try again.")

        self.repository.reset_invalid_login_chance(account.validate_token)

    def login(self, login_dto: LoginDTO):
        account = self.repository.find_by_login_credentials(login_dto)
        if not account:
            raise UnauthorizedException("Token invalid or expired")
        print(account.to_dict())
        self.validate_password(account, login_dto.password)

        self.repository.reset_validate_token(account.account_number)

        return api_response(
            status_code=HTTPStatus.OK,
            message="Login successful",
        )

    def validate_account(self, validate_account_dto: ValidateAccountDTO):
        is_digit_valid = self.validate_check_digit(validate_account_dto.account_number)
        is_branch_valid = int(validate_account_dto.branch) in self.branches

        if not is_digit_valid or not is_branch_valid:
            raise UnauthorizedException("Please check your login details and try again.")

        if self.repository.is_account_blocked(validate_account_dto):
            raise UnauthorizedException("your account is blocked due to excessive login attempts.")

        validate_token = generate_random_token()
        validate_token_expiration_date = datetime.now(timezone.utc) + timedelta(minutes=5)

        updated = self.repository.find_and_update_token(validate_account_dto, validate_token,
                                                        validate_token_expiration_date)

        if not updated:
            raise UnauthorizedException("Please check your login details and try again.")

        print(f"Token '{validate_token}' generated for account {validate_account_dto.account_number}")

        return api_response(
            status_code=HTTPStatus.OK,
            message="Successfully validated Account Number, please proceed to login",
            data={"validate_token": validate_token}
        )

    def validate_check_digit(self, account_number: str):
        account_number_no_cd = int(account_number[:-1])  # remove o ultimo char
        check_digit = int(account_number[-1])  # pega o ultimo char
        calculated_check_digit = self.calculate_check_digit(account_number_no_cd)
        return calculated_check_digit == check_digit

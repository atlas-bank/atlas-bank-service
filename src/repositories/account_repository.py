from datetime import datetime, timezone

from dtos.login_dto import LoginDTO, ValidateAccountDTO
from models.account import Account
from repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)
        self.client = self.db_client.db[self.entity_class.get_collection()]

    @staticmethod
    def get_account_filter(branch, account_number):
        return {'branch': branch, 'account_number': account_number}

    def find_by_cpf(self, cpf: str) -> Account:
        result = self.client.find_one({'cpf': cpf})
        result.pop('_id', None)
        return Account(**result)

    def find_and_update_token(self, validate_account_dto: ValidateAccountDTO, validate_token: str,
                              validate_token_expiration: datetime):
        update = {'$set': {'validate_token': validate_token, 'validate_token_expiration': validate_token_expiration}}

        branch = validate_account_dto.branch
        account_number = validate_account_dto.account_number

        return self.client.find_one_and_update(self.get_account_filter(branch, account_number), update) is not None

    def find_by_login_credentials(self, login_dto: LoginDTO):
        result = self.client.find_one(
            {
                'validate_token': login_dto.validate_token,
                'validate_token_expiration': {'$gt': datetime.now(timezone.utc)}
            }
        )
        if result is None:
            return None
        result.pop('_id', None)
        return Account(**result)

    def reset_validate_token(self, account_number: str):
        self.client.update_one({'account_number': account_number},
                               {'$unset': {'validate_token': "", 'validate_token_expiration': ""}})

    def increase_invalid_login_chance(self, validate_token: str, max_attempts: int):

        filter = {'validate_token': validate_token}
        pipeline = [
            {"$set": {"login_attempt": {"$add": [{"$ifNull": ["$login_attempt", 0]}, 1]}}},
            # caso attemp seja maior ou igual à 5, bloqueia a conta
            {"$set": {"is_blocked": {"$gte": ["$login_attempt", max_attempts]}}}
        ]

        self.client.update_one(filter, pipeline)

    def reset_invalid_login_chance(self, validate_token):
        filter = {'validate_token': validate_token}
        self.client.update_one(filter, {'$set': {'login_attempt': 0}}, )

    def is_account_blocked(self, validate_account_dto: ValidateAccountDTO):
        account_number = validate_account_dto.account_number
        branch = validate_account_dto.branch
        result = self.find_one(self.get_account_filter(branch, account_number), {'is_blocked': 1, '_id': 0})
        if result:
            return result.get('is_blocked', False)

        return False

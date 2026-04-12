from datetime import datetime, timezone

from dtos.login_dto import LoginDTO, ValidateAccountDTO
from models.account import Account
from repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)
        self.client = self.db_client.db[self.entity_class.get_collection()]

    def find_by_cpf(self, cpf: str) -> Account:
        data = self.client.find_one({'cpf': cpf})
        data.pop('_id', None)
        return Account(**data)

    def find_and_update_token(self, validate_account_dto: ValidateAccountDTO, validate_token: str,
                              validate_token_expiration: datetime):
        filter = {'branch': validate_account_dto.branch, 'account_number': validate_account_dto.account_number}
        update = {'$set': {'validate_token': validate_token, 'validate_token_expiration': validate_token_expiration}}

        return self.client.find_one_and_update(filter, update) is not None

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

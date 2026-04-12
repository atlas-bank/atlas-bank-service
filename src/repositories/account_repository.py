from dtos.login_dto import LoginDTO, ValidateAccountDTO
from models.account import Account
from repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)

    def find_by_cpf(self, cpf: str) -> Account:
        collection_name = self.entity_class.get_collection()
        data = self.db_client.db[collection_name].find_one({'cpf': cpf})
        data.pop('_id', None)
        return Account(**data)

    def exists_by_account(self, account: ValidateAccountDTO) -> bool:
        collection_name = self.entity_class.get_collection()
        data = self.db_client.db[collection_name].find_one({
            'branch': account.branch,
            'account_number': account.account_number
        })
        return data is not None

    def find_by_login_credentials(self, login_dto: LoginDTO):
        collection_name = self.entity_class.get_collection()
        data = self.db_client.db[collection_name].find_one(
            {
                'branch': login_dto.branch,
                'account_number': login_dto.account_number,
                'cpf': login_dto.cpf,
                'password': login_dto.password
            }
        )
        if data is None:
            print("não achou conta")
            return None
        data.pop('_id', None)
        return Account(**data)

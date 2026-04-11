from dtos.login_dto import LoginDTO
from models.account import Account
from repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)

    def find_by_cpf(self, cpf: str) -> Account:
        collection_name = self.entity_class.get_collection()
        data = self.db_client.db[collection_name].find_one({'user_cpf': cpf})
        data.pop('_id', None)
        data.pop('password', None)
        return Account(**data)

    def find_by_login_credentials(self, login_dto: LoginDTO):
        collection_name = self.entity_class.get_collection()
        data =  self.db_client.db[collection_name].find_one(
            {
                'agency': login_dto.agency,
                'account': login_dto.account_number,
                'password': login_dto.password
            }
        )
        if data is None:
            return None
        data.pop('_id', None)
        return Account(**data)

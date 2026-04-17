
from models.user import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
        self.client = self.db_client.db[self.entity_class.get_collection()]

    @staticmethod
    def get_user_filter(branch, user):
        return {'branch': branch, 'user': user }

    def find_by_cpf(self, cpf: str) -> User:
        result = self.client.find_one({'cpf': cpf})
        result.pop('_id', None)
        return User(**result)
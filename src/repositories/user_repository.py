
from models.user import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
        self.collection = self.db_client.db[self.entity_class.get_collection()]

    def find_by_cpf(self, cpf: str) -> User | None:
        result = self.collection.find_one({'cpf': cpf})

        if not result:
            return None

        result.pop('_id', None)

        return User(**result)

    def insert(self, user: User):
        return self.collection.insert_one(user.to_dict())

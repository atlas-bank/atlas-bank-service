from models.invest import Invest
from repositories.base_repository import BaseRepository


class InvestRepository(BaseRepository):
    def __init__(self):
        super().__init__(Invest)
        self.client = self.db_client.db[self.entity_class.get_collection()]

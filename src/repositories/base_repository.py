from interfaces.entities_interface import IEntity
from repositories.mongodb_client import MongoDBClient


class BaseRepository:
    def __init__(self, entity_class: type[IEntity]):
        self.db_client = MongoDBClient()
        self.entity_class = entity_class

    def save(self, entity: IEntity):
        return self.db_client.save(entity)

    def find_one(self, query: dict):
        collection_name = self.entity_class.get_collection()
        return self.db_client.db[collection_name].find_one(query)
import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.results import InsertOneResult

from exceptions import InternalServerError
from interfaces.entities_interface import IEntity

url = os.environ.get("MONGODB_URL")
database = os.environ.get("MONGODB_DATABASE")


class MongoDBClient:
    def __init__(self):

        if not url:
            raise InternalServerError("Unable to get MongoDB url")
        try:
            self.db = MongoClient(url)[database]
            self.db.client.admin.command('ping')  # testa conexão com o servidor

        except ConnectionFailure:
            raise InternalServerError("Unable to connect to MongoDB")

    def save(self, entity: IEntity):

        collection = self.db[entity.get_collection()]

        result: InsertOneResult = collection.insert_one(entity.to_dict())

        return result.inserted_id
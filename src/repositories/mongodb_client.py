import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.results import InsertOneResult

from exceptions.exceptions import InternalServerError
from interfaces.entities_interface import IEntity

url = os.environ.get("MONGODB_URL")


class MongoDBClient:
    _client_instance = None

    def __init__(self):

        if not url:
            raise InternalServerError("Unable to get MongoDB url")

        if MongoDBClient._client_instance is None:
            try:
                MongoDBClient._client_instance = MongoClient(url)
                MongoDBClient._client_instance.admin.command('ping')
            except ConnectionFailure:
                MongoDBClient._client_instance = None
                raise InternalServerError("Unable to connect to MongoDB")
        self.client = MongoDBClient._client_instance
        self.db = self.client.get_database()
    def save(self, entity: IEntity):

        collection = self.db[entity.get_collection()]

        result: InsertOneResult = collection.insert_one(entity.to_dict())

        return result.inserted_id

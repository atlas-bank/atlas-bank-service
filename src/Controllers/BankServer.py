import os
from pymongo import MongoClient
from Models.UserModel import User

def Conectar(dados):
    URL = os.getenv('MONGODB_URL')
    client = MongoClient(URL)
    # client = MongoClient("mongodb://localhost:27017/")
    db = client["atlasbank"]
    c = db["clients"]

    novo_usuario = User(**dados)

    usuario_dict = novo_usuario.to_dict()
    c.insert_one(usuario_dict)

    return
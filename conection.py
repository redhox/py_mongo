from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

class MongoAccess : 
    __USER = os.getenv('USER_BDD')
    __PW = os.getenv('PASSWORD')
    __HOST = os.getenv('HOST')
    __PORT = os.getenv('PORT')
    __DB_NAME = os.getenv('BDD')
    __COLLECTION_NAME = os.getenv('COLLECTION')

    @classmethod
    def connexion(cls) :
        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@{cls.__HOST}:{cls.__PORT}")

        cls.db = cls.client[cls.__DB_NAME]
        cls.collection = cls.db[cls.__COLLECTION_NAME]

    @classmethod
    def deconnexion(cls) :
        cls.client.close()

    @classmethod
    def get_element(cls, nom):
        cls.collection.find_one({"nom":nom})
    
    @classmethod
    def get_elements(cls):
        tous = cls.collection.find()
        return list(tous)
    
    @classmethod
    def set_element(cls, nouveau) :
        cls.collection.insert_one(nouveau.to_json())
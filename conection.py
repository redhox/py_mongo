import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
#client = pymongo.MongoClient(f"mongodb://{user_bdd = os.getenv('USER_BDD')}:{password = os.getenv('PASSWORD')}@{host =os.getenv('HOST')}:{port = os.getenv('PORT')}")


host = os.getenv('HOST')
port = os.getenv('PORT')
user = os.getenv('USER_BDD')
password = os.getenv('PASSWORD')

uri = f"mongodb://{user}:{password}@{host}:{port}"
client = pymongo.MongoClient(uri)

db = client.avis
collection = db.films

"""
# Insertion d'un document
document = {
    "title": "Mon article",
    "content": "Ceci est mon article dans MongoDB",
}
collection.insert_one(document)
"""
# Récupération de tous les documents
documents = collection.find()

for document in documents:
    print(document,'\n')

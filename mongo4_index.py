from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['test']
collection = db.users
result = collection.create_index([('user_id', pymongo.ASCENDING)],unique = True)

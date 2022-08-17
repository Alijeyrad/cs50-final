import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')

tests_db = client['Tests']

tests_collection = tests_db['Tests']
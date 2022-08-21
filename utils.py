import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')

tests_db = client['Tests']

tests_collection = tests_db['Tests']

# function to rate neo answers

def rate_answer(answer, key):
    if key == "plus":
        match answer:
            case "Very Accurate":
                return 5
            case "Moderately Accurate":
                return 4
            case "Neither Inaccurate nor Accurate":
                return 3
            case "Moderately Inaccurate":
                return 2
            case "Very Inaccurate":
                return 1
    if key == 'minus':
        match answer:
            case "Very Accurate":
                return 1
            case "Moderately Accurate":
                return 2
            case "Neither Inaccurate nor Accurate":
                return 3
            case "Moderately Inaccurate":
                return 4
            case "Very Inaccurate":
                return 1
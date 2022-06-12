#use mongoDB to store data

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
from pymongo.errors import ServerSelectionTimeoutError
from pymongo.errors import PyMongoError
from pymongo.errors import InvalidDocument

import db

#connect to mongoDB
def connect_mongo() -> object:
    try:
        iclient = MongoClient('mongodb+srv://creditrepair.sxrqct9.mongodb.net/?retryWrites=true&w=majority', 27017)
        print("Connected successfully!!!")
        return iclient
    except ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)
    except ServerSelectionTimeoutError:
        print("Timed out waiting for server")
    except PyMongoError as e:
        print("Error: %s" % e)
#select data from mongoDB

def select_data(collection_name):
    try:
        DB = client['CreditRepair']
        collection = DB[collection_name]
        return collection
    except InvalidDocument as e:
        print("Error: %s" % e)
#select 1 record from mongoDB
def select_one(collection_name,query):
    try:
        collection = db[collection_name]
        record = collection.find_one(query)
        return record
    except InvalidDocument as e:
        print("Error: %s" % e)
#insert data to mongoDB
def insert_data(collection,data):
    try:
        collection.insert_one(data)
    except InvalidDocument as e:
        print("Error: %s" % e)
#update data in mongoDB
def update_data(collection,query,data):
    try:
        collection.update_one(query,data)
    except InvalidDocument as e:
        print("Error: %s" % e)
#delete data in mongoDB
def delete_data(collection,query):
    try:
        collection.delete_one(query)
    except InvalidDocument as e:
        print("Error: %s" % e)


client = connect_mongo();
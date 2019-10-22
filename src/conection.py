from pymongo import MongoClient
import json

def connection(collection):
    MONGO_URL = 'mongodb://avillada-mongodb:oiFUeswHnLGnO1mjEb7fJegXDPaTc8FKbqLwslwy0mYwyqrUG4rso3ffwFTMO0as5PmwRcRubBI5Sr6lhYYCrw==@avillada-mongodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@avillada-mongodb@'
    client = MongoClient(MONGO_URL)
    db = client['taller3']
    collection = db[collection]
    return collection

def db_save(collection, document):
    db_connection = connection(collection)

    insert_response = db_connection.insert(document)

def db_find(collection):
    db_connection = connection(collection)

    try:
        find_response = db_connection.find()
        return find_response
    except:
        return jsonify
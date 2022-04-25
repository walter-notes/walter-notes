import pymongo
import os
import logging



def init_client()-> pymongo.MongoClient:
    username = os.environ.get('MONGO_USER')
    password = os.environ.get('MONGO_PASS')
    url = "mongodb+srv://"+ username+ ":"+ password +"@cluster0.2s8xk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(url)
    return client

def get_database()->pymongo.database.Database:
    client = init_client()
    if client:
        return client.walter
    else:
        return None



def create_walter(databaseInstance):
    # walter = get_database()
    if not walter:
        logger = logging.getLogger(__name__)
        logger.warn("Unable to create walter database. Unable to get instance of database")
        return
    walter.create_collection('page')


def store_page(pageId: str, tags: str):
    page = walter.get_collection('page')
    tags["_id"] = pageId
    page.update_one({ "_id" : pageId }, { "$set": tags}, upsert=True)

walter = get_database()

store_page(1, { "name" : "vishesh"})

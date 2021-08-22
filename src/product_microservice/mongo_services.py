""" Module with various methods for interacting with MongoDb """

from bson.objectid import ObjectId
from pymongo.database import Database


def insert_product(db: Database, data: dict) -> None:
    products = db['products']
    products.insert_one(data)

def get_products(db: Database) -> list:
    data = []
    for product in db['products'].find({'name': 'iphone'}):
        product['_id'] = str(product['_id'])
        data.append(product)
    return data

def get_by_id(db: Database, id:str) -> dict:
    product = db['products'].find_one({'_id': ObjectId(id)})
    if product:
        product['_id'] = str(product['_id'])
        return product
    return None
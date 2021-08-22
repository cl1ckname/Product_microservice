""" Module with various methods for interacting with MongoDb """

from bson.objectid import ObjectId
from pymongo.database import Database


def insert_product(db: Database, data: dict) -> None:
    ''' Creates a document in the Products collection. '''
    products = db['products']
    products.insert_one(data)

def get_all(db: Database) -> list:
    ''' Returns all documents in products collection'''
    data = []
    products = db['products'].find({})
    for product in products:
        product['_id'] = str(product['_id'])
        data.append(product)

    return data

def get_by_id(db: Database, id:str) -> dict:
    ''' Returns document with specified id '''
    product = db['products'].find_one({'_id': ObjectId(id)})
    if product:
        product['_id'] = str(product['_id'])
        return product
    return None

def get_products(db: Database, params: list, sort:str = None, name:str = None):
    ''' Returns document with specified id '''
    data = []
    find_params = {}
    if params:
        find_params['params'] = {'$all':params}
    if sort:
        find_params['params.'+sort] = {'$exists': True}
    if name:
        find_params['name'] = name
    
    products = db['products'].find(find_params)
    if sort:
        if sort == "name":
            products = products.sort(sort)
        else:
            products = products.sort('params.'+sort)

    for product in products:
        product['_id'] = str(product['_id'])
        data.append(product)
    return data
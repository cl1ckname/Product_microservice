from pymongo.database import Database


def insert_product(db: Database, data: dict):
    products = db['products']
    products.insert_one(data)

def get_products(db: Database):
    data = []
    for product in db['products'].find({'name': 'iphone'}):
        product['_id'] = str(product['_id'])
        data.append(product)
    return data
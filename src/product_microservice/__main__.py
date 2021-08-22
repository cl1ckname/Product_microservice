from aiohttp import web
from pymongo import MongoClient
from .mongo_services import get_by_id, insert_product, get_products

print('Trying connect to MongoDB....')
client = MongoClient('localhost:27017')
print('Connection success!')
products_db = client['products']

async def add_product(request: web.Request):
    try:
        if request.content_type == 'application/json':
            data:dict = await request.json()
            name = data['name']
            describe = data['describe']
            params = data.get('params', {})
            insert_product(products_db, {'name': name, 'describe': describe, 'params': params})
            return web.json_response({'status': 'access'}, status=200)
    except (ValueError, KeyError):
        return web.json_response({'status': 'failed', 'message': 'Bad request'}, status=400)

async def get_product(request: web.Request):
    try:
        return web.json_response({'status': 'success', 'data': get_products(products_db)}, status=200)
    except ValueError:
        return web.json_response({'status': 'failed', 'message': 'Bad request'}, status=400)

async def get_product_by_id(request: web.Request):
    try:
        data = await request.json()
        _id = data['id']
        product = get_by_id(_id)
        if not product:
            return web.json_response({'status': 'failed', 'mesage': 'There is no product with this id'}, status=404)
        return web.json_response({'status': 'success', 'data': product}, status=200)
    except ZeroDivisionError:
        return web.json_response({'status': 'failed', 'message': 'Bad request'}, status=400)



app = web.Application()
app.router.add_route('POST', '/', add_product, expect_handler = web.Request.json)
app.router.add_route('GET', '/all', get_product)
app.router.add_route('GET', '/by_id', get_product_by_id)

web.run_app(app)
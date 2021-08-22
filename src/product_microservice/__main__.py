from aiohttp import web
from pymongo import MongoClient
from .mongo_services import get_by_id, insert_product, get_all, get_products

print('Trying connect to MongoDB....')
client = MongoClient('localhost:27017')
print('Connection success!')
products_db = client['products']


def safe_route(func):
    ''' Catches errors during route execution, in case of an error, returns a response json '''
    async def wrapper(*args, **kwargs) -> web.Response:
        try:
            return await func(*args, **kwargs)
        except (ValueError, KeyError):
            return web.json_response({'status': 'failed', 'message': 'Bad request'}, status=400)
    return wrapper


@safe_route
async def add_product(request: web.Request):
    ''' Add product to collection '''
    data: dict = await request.json()
    name = data['name']
    describe = data['describe']
    params = data.get('params', [])
    insert_product(
        products_db, {'name': name, 'describe': describe, 'params': params})
    return web.json_response({'status': 'access'}, status=200)


@safe_route
async def get_all_products(request: web.Request):
    ''' Return all products '''
    return web.json_response({'status': 'success', 'data': get_all(products_db)}, status=200)


@safe_route
async def get_product_by_id(request: web.Request):
    ''' Returns product with the specified id '''
    data = await request.json()
    _id = data['id']
    product = get_by_id(products_db, _id)
    if not product:
        return web.json_response({'status': 'failed', 'mesage': 'There is no product with such params'}, status=404)
    return web.json_response({'status': 'success', 'data': product}, status=200)


@safe_route
async def get_product_by_param(request: web.Request):
    ''' Returns products with the specified parameters and with the specified name '''
    data = await request.json()
    params = data['params']
    sort_by = data.get('sort_by', None)
    products = get_products(products_db, params, sort=sort_by)
    if not products:
        return web.json_response({'status': 'failed', 'mesage': 'There is no product with this id'}, status=404)
    return web.json_response({'status': 'success', 'data': products}, status=200)

app = web.Application()
app.router.add_route('POST', '/add', add_product,
                     expect_handler=web.Request.json)
app.router.add_route('GET', '/all', get_all_products)
app.router.add_route('POST', '/by_id', get_product_by_id,
                     expect_handler=web.Request.json)
app.router.add_route('POST', '/by_param', get_product_by_param,
                     expect_handler=web.Request.json)

web.run_app(app)

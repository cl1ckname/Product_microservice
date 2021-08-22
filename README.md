# Product_microservice
Microservice for adding, removing and retrieving products from MongoDb
## Installing and launching
1. Clone repository  
  `$ git clone https://github.com/cl1ckname/Product_microservice.git`
2. Move to project folder  
  `$ cd Product_microservice`
3. Install requirements  
  `$ pip3 install -r requirements.txt`  
4. (Optional) Run MongoDB  
  `$ docker run -d -p 27017:27017 mongo`
5. Move to source folder  
  `$ cd src`
6. Launch server  
  `$ python3 -m product_microservice`

![demo](https://i.ibb.co/X4YKmXW/git-terminal-demo.gif)

## Endpoints

1. /by_param
  * type: POST
  * data:  
    * `"params": [{"param": value}]` - filter by params
    * `"sort_by": "param"` - parameter or "name". The field by which the sorting will be carried out
    * `"name": "value"` - name constraint
2. /all  
  * type: POST
  * data:  
    * __no data__
3. /by_id
  * type: POST
  * data:
    * `"id": id` - ID of the product


## Examples

1. Add product  
    `$ curl -X POST localhost:8080/
    -H 'Content-Type: application/json'
    -d '{"name":"display","describe":"14", "params":[{"height": 1920}, {"width": 1024}, {"matrix": "IPS"}]}'`  
2. Get all products  
    `$ curl -X GET localhost:8080/all
   -H 'Content-Type: application/json'`
3. Get all monitors with IPS matrix sorted by name  
    `$ curl -X POST localhost:8080/by_param
     -H 'Content-Type: application/json'
     -d '{"params":[{"matrix":"IPS"}], "sort_by":"name"}'`
4. Get product by id  
    `$ curl -X POST localhost:8080/by_id
   -H 'Content-Type: application/json'
   -d '{"id": "61225ec5e72a66d367945106"}'`
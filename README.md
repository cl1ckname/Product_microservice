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

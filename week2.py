from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)


# make the class
class GetAll(Resource):
 def get(self):
  client = MongoClient("mongodb://root:example@localhost:27017/")
  db = client.sales
  collection = db.sales_data
  results = dumps(collection.find())
  return json.loads(results)
api.add_resource(GetAll, '/getAll')
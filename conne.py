from flask import Flask
from flask_restful import Api
from wscrapeapi import Name

app = Flask(__name__)
api = Api(app)


api.add_resource(Name, "/name")

if __name__ == "__main__":
    app.run()
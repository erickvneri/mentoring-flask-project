# TODO:README File and Git the project
# Flask Main Dependencies
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
# DB POOL CONNECTION
import db
# APP RESOURCES
from resources.users import Registry, Account
from resources.products import Products

# APP INIT APP SERVICES
app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app) # TODO: Improve JWT 

# APP CONFIG
app.config['JWT_SECRET_KEY'] = 'Elephants can recognize themselves in the mirror.'

# RESOURCES (ROUTING MODULES)
api.add_resource(Registry, '/create_account')
api.add_resource(Account, '/account')
api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.env = 'development'
    app.debug = True
    app.host = '127.0.0.1'
    app.port = '5000'
    app.run()



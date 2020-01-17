from flask import request, jsonify
from flask_restful import Resource
from services.error import error_response
from services.validation_service import validate_new_product
# from services.db_service import product_query
from services.db_services import product_query
from flask_jwt_extended import jwt_required

class Products(Resource):
    """The product resource will accept Product Queries,
    Creating new products, Updating products prices and
    Removing a product from the API."""
    
    # @jwt_required
    def get(self):
        response = None

        response = product_query(request)
        
        if response is not None:
            return response

        return error_response()

    # TODO:CREATE PRODUCT POST REQUEST
    # @jwt_required
    def post(self):
        response = None

        if validate_new_product():
            return {}, 201
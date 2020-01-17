from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
# Services
from services.validation_service import ( validate_signup, 
validate_signin, validate_delete_account, validate_update_account )
from services.db_services import ( signup_user, signin_user, 
delete_account, update_account )
from services.error import error_response

class Registry(Resource):
    def post(self):
        """ SignUp Handler Class - "/create_account" Endpoint Handler """
        user_data = request.get_json()

        response = None
        if validate_signup():
            response = signup_user(user_data)  
            if response is not None:
                return response
            else:
                return error_response()

class Account(Resource):
    """ This class intend to manage all ACCOUNT OPERATI ON 
        of an already registered user. SIGNIN - UPDATE THE 
        ACCOUNT & REMOVE ACCOUNT. """
    def post(self):
        """ SignIn Handler Class """
        user_data = request.get_json()
        response = None

        if validate_signin():
            response = signin_user(user_data) 
            if response is not None:
                return response
            else:
                return error_response()
    
    @jwt_required
    def delete(self):
        """ Delete Account Class """
        user_data = request.get_json()
        response = None
        
        if validate_delete_account():
            response = delete_account(user_data)
            if response is not None:
                return response
            else:
                return error_response()

    @jwt_required
    def put(self):
        """ Update Account Class """
        user_data = request.get_json()
        response = None

        if validate_update_account():
            response = update_account(user_data)
            if response is not None:
                return response
            else:
                return error_response()
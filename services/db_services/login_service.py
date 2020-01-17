# DB Utilities
from sqlalchemy import exc
from sqlalchemy.orm import Query
from models.users import User
from models.products import Products, Product_Types
from db import Session

import sys
# Other Utilities
from datetime import datetime
from services.error import error_response
from services.response import success_response, product_response

# 
# SIGNUP
# 
def signup_user(user_data):
    '''SignUp Transaction'''
    
    session = Session()
    new_user = User(user_data['username'],
                    user_data['email'], 
                    __hash_pass(user_data['password']),
                    user_data['first_name'], 
                    user_data['last_name'], 
                    datetime.now())
    response = None
    try:
        session.add(new_user)
        session.commit()
        # TRANSACTION SUCCESSFUL
        response = success_response(new_user, 'signup')

    except exc.DBAPIError as e:
        print(e.args)
        session.rollback()
        response = error_response(e.code, e.orig, 'transaction')
    finally:
        return response

# 
# SIGN-IN TRANSACTION
# 
def signin_user(user_data):
    '''SignIn Transaction'''

    session = Session()    
    response = None
    try:
        user = session.query(User).filter( User.email==user_data['email'] ).first()

        if user is not None:
            if __hash_pass(user_data['password']) == user.password:
                user.last_login = datetime.now()
                session.commit()
                # TRANSACTION SUCCESSFUL
                response = success_response(user, 'signin')
            else:
                response = error_response(err_concept='bad_credentials')
        else:
            response = error_response(err_concept='non_user')
    except exc.DBAPIError as e:
        session.rollback()
        response = error_response(e.code, e.orig, 'transaction')
    finally:
        if response is not None:
            return response
# 
# DELETE ACCOUNT TRANSACTION
# 
def delete_account(user_data):
    """Delete user transaction"""

    session = Session()
    response = None
    try:
        user = session.query(User).filter(User.email == user_data['email'] ).first()

        if user is not None:
            if __hash_pass(user_data['password']) == user.password:
                session.delete(user)
                session.commit()
                # TRANSACTION SUCCESSFUL
                response = success_response(user, 'delete')
            else:
                response = error_response(err_concept='bad_credentials')
        else:
            response = error_response(err_concept='non_user')
    
    except exc.DBAPIError as e:
        session.rollback()
        response = error_response(e.code, e.orig, 'transaction')
    
    finally:
        if response is not None:
            return response

# 
# UPDATE ACCOUNT TRANSACTION
# 
def update_account(user_data):
    """Updating user account data"""

    update_data = user_data['new_data']
    session = Session()
    response = None

    try:
        user = session.query(User).filter(User.email == user_data['email']).first()
        
        if user is not None: 
            if __hash_pass(user_data['password']) == user.password:

                if 'email' in update_data:
                    user.email = update_data['email']
                    
                if 'username' in update_data:
                    user.username = update_data['username'] 
                    
                if 'first_name' in update_data:
                    user.first_name = update_data['first_name']
                    
                if 'last_name' in update_data:
                    user.last_name = update_data['last_name']
                    
                if 'password' in update_data:
                    user.password = __hash_pass(update_data['password'])
                    
                user.last_login = datetime.now()
                session.commit()
                # TRANSACTION SUCCESSFUL
                response = success_response(user, 'update')
            else:
                response = error_response(err_concept='bad_credentials')
        else:
            response = error_response(err_concept='non_user')     


    except exc.DBAPIError as e:
        session.rollback()
        response = error_response(e.code, e.orig, 'transaction')

    finally:
        if response is not None:
            return response

def __hash_pass(password):
    '''Method to Hash Password using MD5 Algorythm'''
    import hashlib
    password = password.encode()   
    return hashlib.md5(password).hexdigest()
        
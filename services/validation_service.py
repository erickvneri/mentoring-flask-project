from flask_jwt_extended import create_access_token
from flask_restful import reqparse

def validate_signup():
    """Validate SignUp and SignIn service"""
    parser = reqparse.RequestParser()

    parser.add_argument('username', required=True)
    parser.add_argument('email', required=True)
    parser.add_argument('password', required=True)
    parser.add_argument('first_name', required=True)
    parser.add_argument('last_name', required=True)
    args = parser.parse_args()
    return True

def validate_signin():
    """Validate either Username or Email at payload"""
    parser = reqparse.RequestParser()

    parser.add_argument('email', required=True)
    parser.add_argument('password', required=True)
    args = parser.parse_args()
    return True

def validate_delete_account():
    """Validate params for delete account"""
    parser = reqparse.RequestParser()

    parser.add_argument('email', required=True)
    parser.add_argument('password', required=True)
    parser.add_argument('username', required=True)
    args = parser.parse_args()
    return True

def validate_update_account():
    """Validate params for Updating account"""
    parser = reqparse.RequestParser()

    parser.add_argument('email', required=True)
    parser.add_argument('password', required=True)
    parser.add_argument('username', required=True)
    # POSSIBLE EDIT PARAMS
    parser.add_argument('new_data', required=True, type=dict)

    args = parser.parse_args()
    return True
    
def validate_new_product():
    """Validates data of a new product"""
    parser = reqparse.RequestParser()

    parser.add_argument('name', required=True, type=str)
    parser.add_argument('brand', required=True, type=str)
    parser.add_argument('cost', required=True, type=float)
    parser.add_argument('batch', required=True, type=str)
    parser.add_argument('type', required=True, type=str)
    parser.add_argument('expiration_date', required=True, type=str)
    parser.add_argument('total_products', required=True, type=int)
    args = parser.parse_args()
    return True


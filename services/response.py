from flask import make_response
from flask_jwt_extended import create_access_token
from datetime import datetime
from colorama import Fore 
import json

# PRELOADED TEMPLATES
from templates import success_template

def success_response(data, concept):
    """SUCCESS LOGIN SERVICE RESPONSES"""

    res = success_template[concept]
    res['email'] = data.email
    res['username'] = data.username
    res['first_name'] = data.first_name
    res['last_name'] = data.last_name
    res['last_login'] = str(datetime.now())

    if concept is 'signin':
        res['auth_token'] = create_access_token(identity=f'{data.email}-{data.username}-{data.last_login}')
    
    print(Fore.GREEN, '\n** {} - TRANSACTION COMMITED - {} {}'.format(concept.upper(), data, datetime.now()), Fore.RESET)

    response = make_response( str(res), res['status'] )
    response.headers['Content-Type'] = 'application/json'
    return response

def product_response(data, concept, page=1):
    """PRODUCT RESPONSES"""
    
    res = success_template[concept]
    res['items'] = []
    
    for item in data:
        item_template = {}
        item_template['product'] = item.name.replace(' ', '_')
        item_template['cost'] = float(item.cost)
        item_template['available_units'] = item.total_products
        item_template['expiration_date'] = str(item.expiration_date)
        item_template['batch'] = item.batch
        item_template['type'] = item.type
        res['items'].append(item_template)
    
    res['timestamp'] = str(datetime.now())
    res['page'] = page

    response = make_response( str(res), res['status'] )
    response.headers['Content-Type'] = 'application/json'
    return response



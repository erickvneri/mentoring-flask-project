# DB UTILITIES
from sqlalchemy import exc
from models.products import Products, Product_Types
from db import Session
from sqlalchemy.orm import Query
# UTILITIES
from datetime import datetime
from services.error import error_response
from services.response import success_response, product_response

def product_query(req):
    """ Product Query method. Lazy load the product
        elaborating a Query object before hitting 
        the database. """
    session = Session()
    query = None
    response = None
    page = None
    try:
        query = Query([Products.name, 
                        Products.cost, 
                        Products.total_products, 
                        Products.batch,
                        Products.expiration_date, 
                        Product_Types.name.label('type')]).join(Product_Types)

        if len(req.args) is 0:  
            pass
        else:
            if 'type' in req.args:
                product_type = req.args['type']
                query = query.filter(Product_Types.name == product_type)

            if 'lower_than' in req.args:
                cost = float(req.args['lower_than'])
                query = query.filter(Products.cost < cost)

            if 'higher_than' in req.args:
                cost = float(req.args['higher_than'])
                query = query.filter(Products.cost > cost)

            if 'name' in req.args:
                name = req.args['name']
                query = query.filter(Products.name.like(f'%{name}%'))

    except exc.DBAPIError as e:
        session.rollback()
        response = error_response(e.code, e.orig)

    else:
        if 'page' in req.args:
            page = int(req.args['page'])
            query = query.limit(10).offset( (page - 1) * 10 )
        else:
            page = 1
            query = query.limit(10).offset(0)
        
        query.session = session
        response = product_response(query, 'products_query', page)

    finally:
        return response



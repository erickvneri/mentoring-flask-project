from flask import make_response
from colorama import Fore
from datetime import datetime
import json

# Loaded Template
from templates import error_template

def error_response(code=None, db_description=None, err_concept='connection_err'):
    '''ERROR HANDLER - INTERNAL MESSAGE AND RESPONSE'''
    
    response = error_template[err_concept]
    response['timestamp'] = str(datetime.now())

    # DB TRANSACTION RELATED RESPONSE 
    if code is not None and db_description is not None:
        response['err_code'] = code
        response['description'] = db_description
        internal_message = None
            
        if code is 'e3q8':
            internal_message = f'\n** CONNECTION ERROR'

        elif code is 'gkpj':
            internal_message = f'\n** TRANSACTION ERROR'

        # DB RELATED INTERNAL MESSAGE
        print(Fore.YELLOW, f'{internal_message} - {db_description} {datetime.now()}', Fore.RESET)

    response = make_response( str(response), response['status'] )
    response.headers['Content-Type'] = 'application/json'
    return response

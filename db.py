from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from services.error import error_response
from config import config

from colorama import Fore
from datetime import datetime

connection = None
try:    
    engine = create_engine( config['db_url'], 
                           max_overflow=5, 
                           pool_recycle=3600,
                           pool_size=5 )

    connection = engine.connect()  

except exc.OperationalError as e:
    error_response(e.code, e.orig)   

finally: 
    if connection is not None:
        Session = sessionmaker(bind=engine)
        # CONNECTION ESTABLISHED
        print(Fore.GREEN, f'\n** CONNECTION ESTABLISHED - {datetime.now()}', Fore.RESET)

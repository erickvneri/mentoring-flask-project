from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (ForeignKey, 
Column, String, Integer, TIMESTAMP,
DECIMAL)

Base = declarative_base()

# Product_Types Table
class Product_Types(Base):
    __tablename__ = 'product_types'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(120))

    def __init__(self, name):
        self.name = name

# Products Table
class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, unique=True)
    type_id = Column(Integer, ForeignKey('product_types.id'))
    name = Column(String(120))
    cost = Column(DECIMAL(6,2))
    batch = Column(String(120))
    total_products = Column(Integer)
    expiration_date = Column(TIMESTAMP())

    def __init__(self, type_id, name, cost, batch, total_products, expiration_date):
        self.type_id = type_id
        self.name = name 
        self.cost = cost
        self.batch = batch
        self.total_products = total_products
        self.expiration_date

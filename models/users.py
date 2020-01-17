from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, TIMESTAMP)

Base = declarative_base()

# Users Table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(40), unique=True)
    email = Column(String(40), unique=True)
    password = Column(String(254))
    first_name = Column(String(80))
    last_name = Column(String(80))
    last_login = Column(TIMESTAMP())

    def __init__(self, username, email, password, first_name, last_name, last_login):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.last_login = last_login

    def __repr__(self):
        return '<User(username={}, email={}, first_name={} last_name={}, last_login={})>'.format(self.username, self.email, self.first_name, self.last_name, self.last_login)
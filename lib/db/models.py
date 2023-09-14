from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base() 

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True)
    

class Contact(Base):
    __tablename__= "contacts"

    id = Column(Integer, primary_key=True)
    
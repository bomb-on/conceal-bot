import random

from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

poolBase = declarative_base()

class pool(poolBase):
    __tablename__ = 'pools'
    id          =   Column(Integer, primary_key=True)
    url     =   Column(String(99), unique=True, nullable=False)
    poolurl = Column(String(99), unique=True, nullable=False)
    name      =   Column(String(99), unique=True, default="")
    type      =   Column(String(10), default="normal")    
    hashrate   =   Column(Integer, default=0)
    miners     =   Column(Integer, default=0)

engine = create_engine('sqlite:///poolData.db')

poolBase.metadata.create_all(engine)

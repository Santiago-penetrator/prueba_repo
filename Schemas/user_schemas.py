from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()

class UserS(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True,autoincrement=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    phone = Column(String(15))
    name = Column(String(50))
    image = Column(String(50))
    lastname = Column(String(50))
    type = Column(Integer)

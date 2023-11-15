from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from Schemas.user_schemas import UserS

Base = declarative_base()

class AdrS(Base):
    __tablename__="address"

    id = Column(Integer, primary_key=True,autoincrement=True)
    id_user = Column(Integer, ForeignKey(UserS.id))
    address = Column(String(255))
    neighborhood = Column(String(255))
    lat = Column(Float)
    lng = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
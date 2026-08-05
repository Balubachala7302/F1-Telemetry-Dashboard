from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Driver(Base):
    __tablename__="drivers"
    id=Column(Integer,primary_key=True,index=True)
    driver_number=Column(Integer,unique=True,nullable=False)
    full_name=Column(String,nullable=False)
    team=Column(String)
    Nationality=Column(String)
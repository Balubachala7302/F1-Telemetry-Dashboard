from sqlalchemy import Column,Integer,Float,ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Telemetry(Base):
    __tablename__="telemetry"

    id=Column(Integer,primary_key=True,index=True)
    driver_id=Column(Integer,ForeignKey("drivers.id"),nullable=False)
    lap_number=Column(Integer,nullable=False)

    speed=Column(Float,nullable=False)
    throttle=Column(Float,nullable=False)
    brake=Column(Float,nullable=False)

    gear=Column(Integer,nullable=False)
    rpm=Column(Integer,nullable=False)

    lap_time=Column(Float,nullable=True)

    driver=relationship("Driver")
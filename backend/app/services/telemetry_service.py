from sqlalchemy.orm import Session
from app.models.telemetry import Telemetry
from app.schemas.telemetry import TelemetryCreate

def create_telemetry(db:Session,telemetry:TelemetryCreate):
    db_telemetry=Telemetry(**telemetry.model_dump())
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry


def get_telemetry(db:Session):
    return db.query(Telemetry).all()

def get_telemetry_by_id(db:Session,telemetry_id:int):
    return db.query(Telemetry).filter(Telemetry.id==telemetry_id).first()

def delete_telemetry(db:Session,telemetry_id:int):
    db_telemetry=get_telemetry_by_id(db,telemetry_id)

    if db_telemetry:
        db.delete(db_telemetry)
        db.commit()
    return db_telemetry
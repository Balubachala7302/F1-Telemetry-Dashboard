from sqlalchemy.orm import Session
from app.models.telemetry import Telemetry
from app.schemas.telemetry import TelemetryCreate,TelemetryUpdate

def create_telemetry(db:Session,telemetry:TelemetryCreate):
    db_telemetry=Telemetry(**telemetry.model_dump())
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry


def get_telemetry(db:Session,driver_id:int | None = None,lap_number:int | None = None,skip:int=0,limit:int=100):
    query=db.query(Telemetry)
    if driver_id is not None:
        query=query.filter(Telemetry.driver_id==driver_id)
    if lap_number is not None:
        query=query.filter(Telemetry.lap_number==lap_number)
    return query.offset(skip).limit(limit).all()

def get_telemetry_by_id(db:Session,telemetry_id:int):
    return db.query(Telemetry).filter(Telemetry.id==telemetry_id).first()

def update_telemetry(db:Session,telemetry_id:int,telemetry:TelemetryUpdate):
    db_telemetry=get_telemetry_by_id(db,telemetry_id)
    if not db_telemetry:
        return None

    update_data=telemetry.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(db_telemetry,key,value)
    
    db.commit()
    db.refresh(db_telemetry)
    
    return db_telemetry

def delete_telemetry(db:Session,telemetry_id:int):
    db_telemetry=get_telemetry_by_id(db,telemetry_id)

    if db_telemetry:
        db.delete(db_telemetry)
        db.commit()
    return db_telemetry
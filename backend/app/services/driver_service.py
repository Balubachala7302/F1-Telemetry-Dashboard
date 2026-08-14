from sqlalchemy.orm import Session
from app.models.driver import Driver
from app.schemas.driver import DriverCreate,DriverUpdate

def create_driver(db:Session,driver:DriverCreate):
    db_driver=Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def get_drivers(db:Session):
    return db.query(Driver).all()

def get_driver(db:Session,driver_id:int):
    return db.query(Driver).filter(Driver.id==driver_id).first()

def update_driver(db:Session,driver_id:int,driver:DriverUpdate):
    db_driver=get_driver(db,driver_id)
    if not db_driver:
        return None
    update_data=driver.dict(exclude_unset=True)
    for key,value in update_data.items():
        setattr(db_driver,key,value)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def delete_driver(db:Session,driver_id:int):
    db_driver=get_driver(db,driver_id)
    if db_driver:
        db.delete(db_driver)
        db.commit()
    return db_driver

def get_driver_by_summary(db:Session,driver_id:int):
    from app.models.telemetry import Telemetry
    telemetry=(db.query(Telemetry).filter(Telemetry.driver_id==driver_id).all())
    if not telemetry:
        return None
    lap_times=[t.lap_time for t in telemetry if t.lap_time is not None]
    speeds=[t.speed for t in telemetry]

    return{
        "driver_id":driver_id,
        "total_laps":len(set(t.lap_number for t in telemetry)),
        "fastest_lap":min(lap_times) if lap_times else None,
        "top_speed":max(speeds) if speeds else None,
        "avg_speed":sum(speeds)/len(speeds) if speeds else None,
    }
    
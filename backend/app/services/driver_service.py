from sqlalchemy.orm import Session
from app.models.driver import Driver
from app.schemas.driver import DriverCreate

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


def delete_driver(db:Session,driver_id:int):
    db_driver=get_driver(db,driver_id)
    if db_driver:
        db.delete(db_driver)
        db.commit()
    return db_driver
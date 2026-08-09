from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.schemas.driver import DriverCreate,DriverUpdate,DriverResponse
from app.services.driver_service import create_driver,get_drivers,get_driver,update_driver,delete_driver

router=APIRouter(prefix="/drivers",tags=["Drivers"])

@router.post("/",response_model=DriverResponse)
def create(driver:DriverCreate,db:Session=Depends(get_db)):
    return create_driver(db,driver)

@router.get("/",response_model=list[DriverResponse])
def read_all(db:Session=Depends(get_db)):
    return get_drivers(db)

@router.get("/{driver_id}",response_model=DriverResponse)
def read_one(driver_id:int,db:Session=Depends(get_db)):
    driver=get_driver(db,driver_id)
    if driver is None:
        raise HTTPException(status_code=404,detail="Driver not found")
    return driver

@router.put("/{driver_id}",response_model=DriverResponse)
def update(driver_id:int,driver:DriverUpdate,db:Session=Depends(get_db)):
    updated_driver=update_driver(db,driver_id,driver)
    if updated_driver is None:
        raise HTTPException(status_code=404,detail="Driver not found")
    return updated_driver

@router.delete("/{driver_id}")
def delete(driver_id:int,db:Session=Depends(get_db)):
    driver=delete_driver(db,driver_id)
    if driver is None:
        raise HTTPException(status_code=404,detail="Driver not found")
    return {"message":"Driver deleted successfully"}
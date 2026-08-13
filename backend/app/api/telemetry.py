from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.telemetry import TelemetryCreate,TelemetryUpdate,TelemetryResponse
from app.services.telemetry_service import create_telemetry,get_telemetry,get_telemetry_by_id,update_telemetry,delete_telemetry

router=APIRouter(prefix="/telemetry",tags=["Telemetry"])

@router.post("/",response_model=TelemetryResponse)
def create(telemetry:TelemetryCreate,db:Session=Depends(get_db)):
    return create_telemetry(db,telemetry)

@router.get("/",response_model=list[TelemetryResponse])
def get_all(driver_id:int | None = None,lap_number:int | None = None,skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return get_telemetry(db,driver_id,lap_number,skip,limit)

@router.get("/{telemetry_id}",response_model=TelemetryResponse)
def get_one(telemetry_id:int,db:Session=Depends(get_db)):
    telemetry=get_telemetry_by_id(db,telemetry_id)
    if telemetry is None:
        raise HTTPException(status_code=404,detail="Telemetry not found")
    return telemetry

@router.put("/{telemetry_id}",response_model=TelemetryResponse)
def update(telemetry_id:int,telemetry:TelemetryUpdate,db:Session=Depends(get_db)):
    updated=update_telemetry(db,telemetry_id,telemetry)
    if updated is None:
        raise HTTPException(status_code=404,detail="Telemetry not found")
    return updated

@router.delete("/{telemetry_id}")
def delete(telemetry_id:int,db:Session=Depends(get_db)):
    deleted=delete_telemetry(db,telemetry_id)
    if deleted is None:
        raise HTTPException(status_code=404,detail="Telemetry not found")
    return {
        "message":"Telemetry deleted successfully"
    }
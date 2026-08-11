from pydantic import BaseModel
from typing import Optional

class TelemetryBase(BaseModel):
    driver_id:int
    lap_number:int
    speed:float
    throttle:float
    brake:float
    gear:int
    rpm:int
    lap_time:Optional[float]=None

class TelemetryCreate(TelemetryBase):
    pass

class TelemetryUpdate(TelemetryBase):
    driver_id:Optional[int]=None
    lap_number:Optional[int]=None
    speed:Optional[float]=None
    throttle:Optional[float]=None
    brake:Optional[float]=None
    gear:Optional[int]=None
    rpm:Optional[int]=None
    lap_time:Optional[float]=None

class TelemetryResponse(TelemetryBase):
    id:int

    class Config:
        from_attributes=True
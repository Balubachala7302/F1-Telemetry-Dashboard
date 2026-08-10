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

class TelemetryResponse(TelemetryBase):
    id:int

    class Config:
        from_attributes=True
from pydantic import BaseModel
from typing import Optional

class DriverBase(BaseModel):
    driver_number:int
    full_name:str
    team:str
    Nationality:str

class DriverCreate(DriverBase):
    pass

class DriverUpdate(DriverBase):
    driver_number:Optional[int]=None
    full_name:Optional[str]=None
    team:Optional[str]=None
    Nationality:Optional[str]=None

class DriverResponse(DriverBase):
    id:int

    class Config:
        from_attributes=True
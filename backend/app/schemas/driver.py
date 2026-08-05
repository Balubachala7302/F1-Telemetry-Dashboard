from pydantic import BaseModel

class DriverBase(BaseModel):
    driver_number:int
    full_name:str
    team:str
    Nationality:str

class DriverCreate(DriverBase):
    pass

class DriverResponse(DriverBase):
    id:int
    class Config:
        from_attributes=True
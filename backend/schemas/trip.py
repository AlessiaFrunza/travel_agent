from pydantic import BaseModel
from datetime import date, datetime

class TripCreate(BaseModel):
    usr_id: int
    name: str = None
    budget: float = None
    start_date: date
    end_date: date

class TripUpdate(BaseModel):
    name: str = None
    budget: float = None
    start_date: date = None
    end_date: date = None

class Trip(BaseModel):
    trip_id: int
    usr_id: int
    name: str = None
    budget: float = None
    start_date: date
    end_date: date
    num_day: int
    created_at: datetime

    class Config:
        from_attributes = True
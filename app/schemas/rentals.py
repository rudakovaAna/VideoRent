
from pydantic import BaseModel
from datetime import date
from typing import Optional

class RentalCreate(BaseModel):
    film_id: int
    days: int = 3

class RentalOut(BaseModel):
    id: int
    user_id: int
    film_id: int
    rent_date: date
    due_date: date
    return_date: Optional[date]
    status: str
    late_fee: float
    class Config:
        from_attributes = True

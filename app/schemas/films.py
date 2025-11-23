
from pydantic import BaseModel
from typing import Optional

class FilmBase(BaseModel):
    title: str
    genre: str
    year: int
    copies: int = 1

class FilmCreate(FilmBase):
    pass

class FilmUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    copies: Optional[int] = None

class FilmOut(FilmBase):
    id: int
    class Config:
        from_attributes = True

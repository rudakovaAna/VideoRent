
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api.deps import get_db, require_role
from app.domain.models import Film
from app.schemas.films import FilmCreate, FilmOut, FilmUpdate

router = APIRouter(prefix="/films", tags=["films"])

@router.get("/", response_model=List[FilmOut])
def list_films(q: Optional[str] = Query(default=None), db: Session = Depends(get_db)):
    query = db.query(Film)
    if q:
        query = query.filter(Film.title.ilike(f"%{q}%"))
    return query.order_by(Film.title).all()

@router.post("/", response_model=FilmOut, dependencies=[Depends(require_role("ADMIN"))], status_code=201)
def create_film(film_in: FilmCreate, db: Session = Depends(get_db)):
    film = Film(**film_in.model_dump())
    db.add(film)
    db.commit()
    db.refresh(film)
    return film

@router.put("/{film_id}", response_model=FilmOut, dependencies=[Depends(require_role("ADMIN"))])
def update_film(film_id: int, film_upd: FilmUpdate, db: Session = Depends(get_db)):
    film = db.query(Film).get(film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    for k, v in film_upd.model_dump(exclude_unset=True).items():
        setattr(film, k, v)
    db.commit()
    db.refresh(film)
    return film

@router.delete("/{film_id}", status_code=204, dependencies=[Depends(require_role("ADMIN"))])
def delete_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(Film).get(film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    db.delete(film)
    db.commit()
    return None

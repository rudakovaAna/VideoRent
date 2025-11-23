
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.api.deps import get_db, get_current_user
from app.domain.models import Rental, Film, RentalStatus, User
from app.schemas.rentals import RentalCreate, RentalOut

router = APIRouter(prefix="/rentals", tags=["rentals"])

@router.post("/", response_model=RentalOut, status_code=201)
def start_rental(body: RentalCreate, db: Session = Depends(get_db), payload: dict = Depends(get_current_user)):
    user_id = int(payload["sub"])
    film = db.query(Film).get(body.film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    # availability check
    active_count = db.query(Rental).filter(Rental.film_id == film.id, Rental.status == RentalStatus.ACTIVE).count()
    if active_count >= film.copies:
        raise HTTPException(status_code=409, detail="No copies available")    
    rental = Rental(user_id=user_id, film_id=film.id, rent_date=date.today(), due_date=date.today() + timedelta(days=body.days), status=RentalStatus.ACTIVE, late_fee=0)
    db.add(rental)
    db.commit()
    db.refresh(rental)
    return rental

@router.post("/{rental_id}/return", response_model=RentalOut)
def return_rental(rental_id: int, db: Session = Depends(get_db), payload: dict = Depends(get_current_user)):
    rental = db.query(Rental).get(rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    if rental.user_id != int(payload["sub"]):
        raise HTTPException(status_code=403, detail="Forbidden")
    if rental.return_date:
        return rental
    rental.return_date = date.today()
    # simple late fee rule: 1 PLN per day
    if rental.return_date > rental.due_date:
        delta = (rental.return_date - rental.due_date).days
        rental.late_fee = round(float(delta) * 1.0, 2)
        rental.status = RentalStatus.LATE
    else:
        rental.status = RentalStatus.RETURNED
    db.commit()
    db.refresh(rental)
    return rental

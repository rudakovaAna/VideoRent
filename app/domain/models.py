
from datetime import date
from sqlalchemy import String, Integer, Date, Enum, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum as PyEnum
from typing import Optional
from .security import hash_password
from app.infra.db import Base

class Role(str, PyEnum):
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"

class RentalStatus(str, PyEnum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    LATE = "LATE"

class PaymentStatus(str, PyEnum):
    PENDING = "PENDING"
    PAID = "PAID"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.CLIENT)
    rentals: Mapped[list["Rental"]] = relationship(back_populates="user")

    @staticmethod
    def create(email: str, password: str, first_name: str, last_name: str, role: Role = Role.CLIENT):
        return User(
            email=email,
            password_hash=hash_password(password),
            first_name=first_name,
            last_name=last_name,
            role=role
        )

class Film(Base):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    genre: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)
    copies: Mapped[int] = mapped_column(Integer, default=1)
    rentals: Mapped[list["Rental"]] = relationship(back_populates="film")

class Rental(Base):
    __tablename__ = "rentals"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    film_id: Mapped[int] = mapped_column(ForeignKey("films.id"))
    rent_date: Mapped[date] = mapped_column(Date)
    due_date: Mapped[date] = mapped_column(Date)
    return_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    late_fee: Mapped[float] = mapped_column(Numeric(10,2), default=0)
    status: Mapped[RentalStatus] = mapped_column(Enum(RentalStatus), default=RentalStatus.ACTIVE)

    user: Mapped[User] = relationship(back_populates="rentals")
    film: Mapped[Film] = relationship(back_populates="rentals")

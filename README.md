VideoRent – System Wypożyczalni Kaset Video

Projekt realizowany w ramach przedmiotu Metodyki Wytwarzania Oprogramowania. System umożliwia zarządzanie wypożyczeniami kaset video: rejestrację użytkowników, katalog filmów, wypożyczenia, zwroty oraz naliczanie opłat.

✅ Funkcjonalności

Rejestracja i logowanie użytkowników (JWT)

Role użytkowników: CLIENT / ADMIN

Zarządzanie katalogiem filmów (CRUD)

Wypożyczenia, zwroty i naliczanie opłat za zwłokę

Rezerwacje filmów i kolejka oczekujących

Raporty dla administratora

REST API (FastAPI)


🏗️ Architektura

Architektura warstwowa (MVC + REST)

Wzorce: Factory, Singleton, Observer

Baza: SQLite (dev) / PostgreSQL (prod)

Testy: pytest (unit + integration)

Konteneryzacja: Docker / Docker Compose
Client → REST API → Services → Repository → Database


🛠️ Stack technologiczny

Python 3.11, FastAPI

SQLAlchemy, Alembic

Pydantic, PyJWT, bcrypt

pytest, httpx

Docker, docker-compose

PlantUML (diagramy UML)

Autorzy
Anastazja Rudakowa, Zlata Bohdan


VideoRent – System Wypożyczalni Kaset Video

Projekt zrealizowany w ramach przedmiotu Metodyki Wytwarzania Oprogramowania.
Celem projektu było zaprojektowanie i zaimplementowanie systemu informacyjnego wspomagającego działanie wypożyczalni kaset video, z wykorzystaniem nowoczesnych technologii webowych oraz zwinnej metodyki wytwarzania oprogramowania.

🎯 Cel projektu

System umożliwia obsługę podstawowych procesów biznesowych wypożyczalni kaset video, takich jak:

rejestracja i logowanie użytkowników,

zarządzanie katalogiem filmów,

realizacja wypożyczeń i zwrotów,

kontrola dostępu na podstawie ról użytkowników.

Projekt ma charakter edukacyjny i demonstracyjny.

✅ Funkcjonalności

Rejestracja użytkowników

Logowanie użytkowników z wykorzystaniem JWT

Role użytkowników: CLIENT oraz ADMIN

Przeglądanie katalogu filmów

Wypożyczanie i zwracanie kaset video

Podstawowa kontrola dostępności kaset

REST API z automatyczną dokumentacją (Swagger UI)

🏗️ Architektura systemu

System został zaprojektowany w oparciu o:

Architekturę warstwową

warstwa API (endpointy REST),

warstwa logiki biznesowej,

warstwa dostępu do danych (ORM + baza danych).

REST API

komunikacja poprzez protokół HTTP,

format danych: JSON.

Dependency Injection

mechanizm wstrzykiwania zależności dostępny w frameworku FastAPI.

🛠️ Technologie

Język programowania: Python 3

Framework webowy: FastAPI

Serwer aplikacyjny: Uvicorn

ORM: SQLAlchemy

Baza danych: SQLite

Walidacja danych: Pydantic

Autoryzacja: JWT (JSON Web Token)

Testy: pytest

Dokumentacja API: Swagger UI (OpenAPI)

▶️ Uruchomienie aplikacji
1. Aktywacja środowiska wirtualnego
cd VideoRent
source .venv/bin/activate

2. Instalacja zależności
pip install -r requirements.txt

3. Utworzenie bazy danych
rm -f videorent.db

python3 - <<'PY'
from app.infra.db import get_engine, Base
from app.domain import models
engine = get_engine()
Base.metadata.create_all(bind=engine)
print("Baza danych gotowa")
PY

4. Uruchomienie serwera
python3 -m uvicorn app.main:app --host 127.0.0.1 --port 8000

🧪 Testowanie

Testy manualne realizowane z wykorzystaniem Swagger UI

Testy jednostkowe i integracyjne realizowane przy użyciu pytest

Dokumentacja API dostępna pod adresem:

http://127.0.0.1:8000/docs

📄 Dokumentacja

Projekt zawiera pełną dokumentację obejmującą:

opis wymagań funkcjonalnych i niefunkcjonalnych,

opis zastosowanej metodyki (Scrum),

opis architektury systemu,

opis testów i przypadków testowych,

wnioski i możliwe kierunki rozwoju.

👤 Autorzy

Anastazja Rudakowa; Zlata Bohdan

from fastapi import FastAPI
from app.infra.db import get_engine, Base
from app.api import auth, films, rentals

def create_app() -> FastAPI:
    app = FastAPI(title="VideoRent API", version="0.1.0")
    # Create tables on startup (demo)
    engine = get_engine()
    Base.metadata.create_all(bind=engine)

    app.include_router(auth.router)
    app.include_router(films.router)
    app.include_router(rentals.router)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app

app = create_app()

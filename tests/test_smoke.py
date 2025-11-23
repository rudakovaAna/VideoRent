
from fastapi.testclient import TestClient
from app.main import app
from app.infra.db import Base, get_engine

client = TestClient(app)

def setup_module(module):
    # fresh DB per test module (sqlite file gets reset by re-creating tables)
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

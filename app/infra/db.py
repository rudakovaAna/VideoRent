
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from contextlib import contextmanager

DB_URL = os.getenv("DB_URL", "sqlite:///./videorent.db")

class Base(DeclarativeBase):
    pass

_engine = None
_SessionLocal = None

def get_engine():
    global _engine
    if _engine is None:
        connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}
        _engine = create_engine(DB_URL, echo=False, future=True, connect_args=connect_args)
    return _engine

def get_session_maker():
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    return _SessionLocal

@contextmanager
def session_scope():
    Session = get_session_maker()
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

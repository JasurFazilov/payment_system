from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@databse/postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from database import models

def get_db():
    db = SessionLocal()

    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
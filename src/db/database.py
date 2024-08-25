from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

DATABASE_URL = 'postgresql://myuser:mypassword@db:5432/docker_postgres'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db()-> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
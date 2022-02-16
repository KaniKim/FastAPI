from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str

    class Config:
        env_file = ".env"


settings = Settings()

SQLACLHEMY_DATABASE_URL = settings.db_url

engine = create_engine(SQLACLHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

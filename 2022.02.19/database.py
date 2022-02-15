from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACLHEMY_DATABASE_URL = "postgreqsl://kanikim:rlarhksgml!4113@laoclhost:5432/fast"

engine = create_engine(SQLACLHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

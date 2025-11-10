from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.air_quality import Base

engine = create_engine("sqlite:///air_quality.db")
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

# models/air_quality_record.py (combined version)
from sqlalchemy import Column, Integer, String, Float, DateTime, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AirQualityRecord(Base):
    __tablename__ = 'air_quality_records'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    country = Column(String)
    parameter = Column(String)
    value = Column(Float)
    unit = Column(String)
    date_utc = Column(DateTime)

    __table_args__ = (
        UniqueConstraint('location', 'parameter', 'date_utc', name='uq_measurement'),
    )

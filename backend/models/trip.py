from sqlalchemy import Column, Integer, String, Numeric, Date, TIMESTAMP, Computed
from sqlalchemy.sql import func
from database import Base

class Trip(Base):
    __tablename__ = "Trip"

    trip_id = Column(Integer, primary_key=True, index=True)
    usr_id = Column(Integer, nullable=False)
    name = Column(String(150))
    budget = Column(Numeric(10,2))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    num_day = Column(Integer, Computed("end_date - start_date"))
    created_at = Column(TIMESTAMP, server_default=func.now())
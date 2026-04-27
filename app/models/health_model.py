from app.db.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class HealthModel(BaseModel):
    __tablename__ = "health"
    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False)
    message = Column(String(50), nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
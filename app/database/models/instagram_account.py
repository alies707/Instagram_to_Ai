from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base

class InstagramAccount(Base):
    __tablename__ = "instagram_accounts"

    id = Column(Integer, primary_key=True)
    instagram_id = Column(String, unique=True, nullable=False)
    page_id = Column(String)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

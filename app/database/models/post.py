from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    instagram_account_id = Column(Integer, nullable=False)
    image_url = Column(String, nullable=False)
    caption = Column(String)
    status = Column(String, default="draft")
    scheduled_at = Column(DateTime)
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base

class OAuthToken(Base):
    __tablename__ = "oauth_tokens"

    id = Column(Integer, primary_key=True)
    instagram_account_id = Column(Integer, nullable=False)
    encrypted_token = Column(String, nullable=False)
    expires_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

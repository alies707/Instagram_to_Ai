from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class InstagramAccount(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    account_id: Mapped[str] = mapped_column(String(100))
    access_token: Mapped[str] = mapped_column(Text)


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    caption: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(50), default="draft")
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

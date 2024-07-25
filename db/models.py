from typing import Optional
from sqlalchemy import String
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(100), default="")
    words: Mapped[str] = mapped_column(String(1000), default="")
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "words": self.words,
            "created_at": self.created_at.strftime(
                "%d %B %Y, %I:%M %p") if self.created_at else None,
        }

    def __repr__(self) -> str:
        return f"<Words(name={self.name}, description={self.description})>"

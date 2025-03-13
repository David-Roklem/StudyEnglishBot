from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base

if TYPE_CHECKING:
    from .question import Question


class Level(Base):
    __tablename__ = "levels"
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    question: Mapped["Question"] = relationship(back_populates="level")

    def __repr__(self) -> str:
        return f"Level(id={self.id!r}, name={self.name})"

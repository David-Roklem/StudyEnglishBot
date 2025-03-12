from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey
from .base import Base

if TYPE_CHECKING:
    from .answer import Answer
    from .level import Level


class Question(Base):
    __tablename__ = "questions"
    text: Mapped[str] = mapped_column(Text, nullable=False)
    level_id: Mapped[uuid4] = mapped_column(ForeignKey("levels.id"), nullable=False)
    subcategory_id: Mapped[uuid4] = mapped_column(ForeignKey("subcategories.id"), nullable=False)
    answers: Mapped[list["Answer"]] = relationship(back_populates="question")
    level: Mapped[list["Level"]] = relationship(back_populates="question")

from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey, Boolean
from .base import Base

if TYPE_CHECKING:
    from .question import Question


class Answer(Base):
    __tablename__ = "answers"
    text: Mapped[str] = mapped_column(Text, nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    question_id: Mapped[uuid4] = mapped_column(ForeignKey("questions.id"), nullable=False)
    question: Mapped["Question"] = relationship(back_populates="answers")

    def __repr__(self):
        return f"Answer(text={self.text}, is_correct={self.is_correct})"

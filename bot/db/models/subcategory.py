from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from .base import Base

if TYPE_CHECKING:
    from .category import Category


class Subcategory(Base):
    __tablename__ = "subcategories"
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    category_id: Mapped[uuid4] = mapped_column(ForeignKey("categories.id"), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="subcategories")

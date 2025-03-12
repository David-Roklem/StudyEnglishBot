from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base

if TYPE_CHECKING:
    from .subcategory import Subcategory


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    subcategories: Mapped[list["Subcategory"]] = relationship(back_populates="category")

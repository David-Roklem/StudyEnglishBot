from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, DateTime, String, Text, func, Uuid, text


class Base(DeclarativeBase):
    id: Mapped[uuid4] = mapped_column(
        Uuid,
        primary_key=True,
        unique=True,
        default=uuid4,
        server_default=text("gen_random_uuid()"),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
    )


class User(Base):
    __tablename__ = "users"
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=True)
    last_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(30), unique=True, nullable=True)
    email: Mapped[str | None] = mapped_column(String(100), unique=True, nullable=True)
    # на уровне Алхимии email никак не валидировать, нужно делать на уровне прилож (Пайдантик)

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, telegram_id={self.telegram_id}, first_name={self.first_name!r}, "
                f"last_name={self.last_name!r}, phone_number={self.phone_number!r}, email={self.email!r})")

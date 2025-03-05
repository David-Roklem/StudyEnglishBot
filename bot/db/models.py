from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.schema import CreateTable
from sqlalchemy import BigInteger, DateTime, String, Text, func, Uuid


class Base(DeclarativeBase):
    id: Mapped[uuid4] = mapped_column(
        Uuid,
        primary_key=True,
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        onupdate=func.now(),
    )


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=True)
    last_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(50), unique=True, nullable=True)
    email: Mapped[str | None] = mapped_column(String(100), unique=True, nullable=True)
    # на уровне Алхимии никак не валидировать, нужно делать на уровне прилож (Пайдантик)


# async def main():
#     engine = create_engine(
#         # Строка подключения при использовании Docker-образов из репозитория
#         # В противном случае подставьте свои значения
#         url="postgresql+psycopg://postgres:100200@127.0.0.1:5431/postgres",
#         echo=False
#     )

#     # Печатает на экран SQL-запрос для создания таблицы в PostgreSQL
#     print(CreateTable(User.__table__).compile(dialect=postgresql.dialect()))

#     # Удаление предыдущей версии базы
#     # и создание таблиц заново
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)


# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())

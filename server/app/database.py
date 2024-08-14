from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import settings


DB_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_async_engine(DB_URL)

create_async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class MigrationBase(DeclarativeBase):
    pass

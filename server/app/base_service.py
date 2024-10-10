from sqlalchemy import select, insert

from database import create_async_session, MigrationBase


class BaseService:
    model: MigrationBase

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with create_async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with create_async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with create_async_session() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_one(cls, **data):
        async with create_async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

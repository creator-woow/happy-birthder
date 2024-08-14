from sqlalchemy import Column, Integer, String, Date, ForeignKey

from database import MigrationBase


class Profiles(MigrationBase):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    birth_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    avatar_id = Column(Integer)


from sqlalchemy import Column, Integer, String, ForeignKey

from database import MigrationBase


class Gifts(MigrationBase):
    __tablename__ = "gifts"

    id = Column(Integer, primary_key=True)
    message = Column(String)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recipient_id = Column(Integer, ForeignKey("users.id"), nullable=False)

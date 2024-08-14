from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from fastapi import Query

from database import MigrationBase


class Users(MigrationBase):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(100), nullable=False)
    hashed_password = mapped_column(String(100), nullable=False)


class GetUsersArgs:
    def __init__(
            self,
            page: Optional[int] = Query(None, gt=0),
            page_size: Optional[int] = Query(None, gt=10),
    ):
        self.page = page
        self.page_size = page_size

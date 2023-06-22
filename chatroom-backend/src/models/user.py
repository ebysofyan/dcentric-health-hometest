from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import BaseIntPrimaryKey


class User(BaseIntPrimaryKey):
    __tablename__ = "user__user"

    name: Mapped[str] = mapped_column(String(50), nullable=False)

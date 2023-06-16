from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseIntPrimaryKey


class Room(BaseIntPrimaryKey):
    __tablename__ = "chat__room"

    name: Mapped[str] = mapped_column(String(50), unique=True)
    slug: Mapped[str] = mapped_column(String(60), unique=True)
    encryption_key: Mapped[str] = mapped_column(String(40))
    creator_id: Mapped[int | None] = mapped_column(
        Integer(), ForeignKey("user__user.id"), nullable=True
    )


class Chat(BaseIntPrimaryKey):
    __tablename__ = "chat__chat"

    text: Mapped[str] = mapped_column(String())
    room_id: Mapped[int] = mapped_column(Integer(), ForeignKey("chat__room.id"))
    sender_id: Mapped[int] = mapped_column(Integer(), ForeignKey("user__user.id"))

    room: Mapped["Room"] = relationship(uselist=False)
    sender: Mapped["User"] = relationship(uselist=False)

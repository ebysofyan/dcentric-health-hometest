import datetime
from typing import Any, Self

from pydantic import BaseModel, root_validator

from entity.user import UserEntity


class RoomEntity(BaseModel):
    id: int
    name: str
    encryption_key: str

    class Config:
        orm_mode = True


class DetailRoomEntity(RoomEntity):
    user: UserEntity | None

    class Config:
        orm_mode = False


class CreateRoomEntity(BaseModel):
    name: str
    creator_id: int | None = None


class JoinRoomEntity(BaseModel):
    name: str


class ChatEntity(BaseModel):
    text: str
    room_id: int
    sender: UserEntity
    created_at: datetime.datetime

    @root_validator
    def format_created_at(cls: Self, values: dict[str, Any]) -> str:
        created_at = values.get("created_at")
        if created_at is not None:
            values["created_at"] = created_at.strftime("%d %b %H:%M %p")
        return values

    class Config:
        orm_mode = True


class CreateChatEntity(BaseModel):
    text: str
    room_id: int
    sender_id: int

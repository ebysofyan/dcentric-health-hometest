import datetime

from pydantic import BaseModel

from entity.user import UserEntity


class RoomEntity(BaseModel):
    id: int
    name: str
    encryption_key: str
    user: UserEntity | None

    # class Config:
    #     orm_mode = True


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

    class Config:
        orm_mode = True


class CreateChatEntity(BaseModel):
    text: str
    room_id: int
    sender_id: int

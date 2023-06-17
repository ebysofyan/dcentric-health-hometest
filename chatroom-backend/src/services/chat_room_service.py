import sqlite3

import sqlalchemy.exc as sqlalchemy_exception
from entity.chat import CreateRoomEntity
from fastapi import HTTPException, status
from models.chat import Room
from repositories.chat_room_repository import ChatRoomRepository


class ChatRoomService:
    def __init__(self, chat_room_repository: ChatRoomRepository) -> None:
        self._chatroom_repository: ChatRoomRepository = chat_room_repository

    def get_all(self) -> list[Room]:
        return self._chatroom_repository.get_all()

    def get_by_name(self, name: str) -> Room | None:
        return self._chatroom_repository.get_by_name(name=name)

    def create(self, payload: CreateRoomEntity, commit: bool = True) -> Room:
        try:
            return self._chatroom_repository.create(payload=payload, commit=commit)
        except (sqlalchemy_exception.IntegrityError, sqlite3.IntegrityError):
            self._chatroom_repository._db_session.close()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Room already exist"
            )
        except Exception as e:
            self._chatroom_repository._db_session.close()
            raise e

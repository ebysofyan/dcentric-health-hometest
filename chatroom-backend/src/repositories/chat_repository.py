from entity.chat import CreateChatEntity
from internal.types import ScopedSession
from models.chat import Chat, Room


class ChatRepository:
    def __init__(self, db_session: ScopedSession) -> None:
        self._db_session = db_session

    def get_all_by_room(self, room_name: str) -> list[Chat]:
        return self._db_session.query(Chat).join(Chat.room).filter(Room.name == room_name).all()

    def create(self, payload: CreateChatEntity, commit: bool = True) -> Chat:
        chat = Chat(text=payload.text, room_id=payload.room_id, sender_id=payload.sender_id)
        self._db_session.add(chat)
        if commit:
            self._db_session.commit()
        return chat

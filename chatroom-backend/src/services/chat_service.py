from entity.chat import CreateChatEntity
from models.chat import Chat
from repositories.chat_repository import ChatRepository


class ChatService:
    def __init__(self, chat_repository: ChatRepository) -> None:
        self._chat_repository: ChatRepository = chat_repository

    def get_all_by_room(self, room_id: int) -> list[Chat]:
        return self._chat_repository.get_all_by_room(room_id=room_id)

    def create(self, payload: CreateChatEntity, commit: bool = True) -> Chat:
        try:
            # enc_text: str = chiper_utils.encrypt(plaintext=payload.text)
            return self._chat_repository.create(
                payload=payload,
                commit=commit,
            )
        except Exception as e:
            self._chat_repository._db_session.close()
            raise e

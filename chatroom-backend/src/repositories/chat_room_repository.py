import uuid

from entity.chat import CreateRoomEntity
from internal.types import ScopedSession
from models.chat import Room
from slugify import slugify


class ChatRoomRepository:
    def __init__(self, db_session: ScopedSession) -> None:
        self._db_session = db_session

    def get_all(self) -> list[Room]:
        return self._db_session.query(Room).all()

    def get_by_name(self, name: str) -> Room | None:
        return (
            self._db_session.query(Room)
            .filter(Room.slug == slugify(text=name, allow_unicode=True))
            .first()
        )

    def create(self, payload: CreateRoomEntity, commit: bool = True) -> Room:
        room = Room(
            name=payload.name,
            slug=slugify(text=payload.name, allow_unicode=True),
            encryption_key=uuid.uuid4().hex,
            creator_id=payload.creator_id,
        )
        self._db_session.add(room)
        if commit:
            self._db_session.commit()
        return room

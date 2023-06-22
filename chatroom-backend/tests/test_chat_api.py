import uuid

from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from internal.types import ScopedSession
from models.chat import Chat, Room
from models.user import User


def test_GET_get_all_chats_by_room_api_should_return_200(
    client: TestClient, db_session: ScopedSession
) -> None:
    room = Room(name="Room", slug="room", encryption_key=uuid.uuid4().hex)
    db_session.add(room)

    sender = User(name="User 1")
    db_session.add(sender)
    db_session.flush()

    for i in range(10):
        chat = Chat(text=f"Chat {i}", room_id=room.id, sender_id=sender.id)
        db_session.add(chat)
    db_session.commit()

    response: Response = client.get(f"/chats/{room.id}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10

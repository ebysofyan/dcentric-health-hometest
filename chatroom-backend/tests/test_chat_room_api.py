import uuid

from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from internal.types import ScopedSession
from models.chat import Room


def test_POST_create_new_room_api_success_should_return_200(client: TestClient) -> None:
    response: Response = client.post("/rooms", json={"name": "New room", "creator_id": None})
    assert response.status_code == status.HTTP_200_OK


def test_GET_get_all_rooms_api_success_should_return_200(client: TestClient, db_session) -> None:
    for i in range(10):
        enc_key: str = uuid.uuid4().hex
        room = Room(name=f"Room {i}", slug=f"room-{i}", encryption_key=enc_key)
        db_session.add(room)
    db_session.commit()

    response: Response = client.get("/rooms")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_POST_join_existing_room_api_success_should_return_200(
    client: TestClient, db_session: ScopedSession
) -> None:
    room = Room(name="Room", slug="room", encryption_key=uuid.uuid4().hex)
    db_session.add(room)
    db_session.commit()

    response: Response = client.post("/rooms/join", json={"name": room.name})
    assert response.status_code == status.HTTP_200_OK


def test_POST_join_existing_room_api_failed_should_return_404(
    client: TestClient, db_session: ScopedSession
) -> None:
    response: Response = client.post("/rooms/join", json={"name": "Some name"})
    assert response.status_code == status.HTTP_404_NOT_FOUND

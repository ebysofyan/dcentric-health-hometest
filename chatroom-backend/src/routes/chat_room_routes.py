import uuid

from dependency_injector.wiring import Provide, inject
from deps_container import Container
from entity.chat import CreateRoomEntity, JoinRoomEntity, RoomEntity
from entity.user import CreateUserEntity
from fastapi import APIRouter, Depends, HTTPException, status
from models.chat import Room
from models.user import User
from services.chat_room_service import ChatRoomService
from services.user_service import UserService

router = APIRouter(prefix="/rooms")


@router.get("", response_model=list[RoomEntity])
@inject
async def get_rooms(
    chat_room_service: ChatRoomService = Depends(Provide[Container.chat_room_service]),
) -> list[Room]:
    print(chat_room_service.get_all())
    return chat_room_service.get_all()


@router.post("", response_model=RoomEntity)
@inject
async def create_new_room(
    payload: CreateRoomEntity,
    chat_room_service: ChatRoomService = Depends(Provide[Container.chat_room_service]),
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Room:
    try:
        hex: str = uuid.uuid4().hex
        user: User = user_service.create(payload=CreateUserEntity(name=f"User#{hex[:8]}"))
        room: Room = chat_room_service.create(
            payload=CreateRoomEntity(name=payload.name, creator_id=user.id), commit=True
        )
        return {
            "id": room.id,
            "name": room.name,
            "encryption_key": room.encryption_key,
            "user": {"id": user.id, "name": user.name},
        }
    except Exception as e:
        raise e


@router.post("/join", response_model=RoomEntity)
@inject
async def join_room(
    payload: JoinRoomEntity,
    chat_room_service: ChatRoomService = Depends(Provide[Container.chat_room_service]),
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Room:
    try:
        room: Room | None = chat_room_service.get_by_name(name=payload.name)
        if room is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")

        hex: str = uuid.uuid4().hex
        user: User = user_service.create(payload=CreateUserEntity(name=f"User#{hex[:8]}"))
        return {
            "id": room.id,
            "name": room.name,
            "encryption_key": room.encryption_key,
            "user": {"id": user.id, "name": user.name},
        }
    except Exception as e:
        raise e

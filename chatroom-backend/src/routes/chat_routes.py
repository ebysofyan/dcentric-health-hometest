from dependency_injector.wiring import Provide, inject
from deps_container import Container
from entity.chat import ChatEntity
from fastapi import APIRouter, Depends
from models.chat import Chat
from services.chat_service import ChatService

router = APIRouter(prefix="/chats")


@router.get("/{room_id}", response_model=list[ChatEntity])
@inject
async def get_chats(
    room_id: int,
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> list[Chat]:
    return chat_service.get_all_by_room(room_id=room_id)

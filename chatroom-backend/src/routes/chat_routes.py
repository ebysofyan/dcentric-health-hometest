from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from deps_container import Container
from entity.chat import ChatEntity
from models.chat import Chat
from services.chat_service import ChatService

router = APIRouter(prefix="/chats")


@router.get("/{room_name}", response_model=list[ChatEntity])
@inject
async def get_chats(
    room_name: str,
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> list[Chat]:
    return chat_service.get_all_by_room(room_name=room_name)

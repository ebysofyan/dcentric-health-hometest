from typing import Any

from core import logger
from dependency_injector.wiring import Provide, inject
from deps_container import Container
from entity.chat import CreateChatEntity
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from models.chat import Chat
from services.chat_service import ChatService
from ws_connection_manager import ConnectionManager

router = APIRouter(prefix="/ws")


@router.websocket("/{room_id}")
@inject
async def websocket_endpoint(
    websocket: WebSocket,
    room_id: int,
    connection_manager: ConnectionManager = Depends(Provide[Container.connection_manager]),
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> None:
    await connection_manager.connect(room_id=room_id, websocket=websocket)
    try:
        while True:
            data = await websocket.receive_json()
            chat: Chat = chat_service.create(
                payload=CreateChatEntity(
                    text=data["text"], room_id=room_id, sender_id=data["sender_id"]
                )
            )
            response_data: dict[str, Any] = {
                "text": chat.text,
                "room_id": chat.room_id,
                "sender": {"id": chat.sender_id, "name": chat.sender.name},
                "created_at": chat.created_at.strftime("%d %b %H:%M %p"),
            }
            await connection_manager.broadcast(room_id=room_id, data=response_data)
    except WebSocketDisconnect:
        connection_manager.disconnect(room_id=room_id, websocket=websocket)
        logger.info("Disconnected from websocket")

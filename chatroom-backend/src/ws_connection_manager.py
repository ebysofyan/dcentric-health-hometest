from typing import Any

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections_map: dict[int, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        try:
            self.active_connections_map[room_id].append(websocket)
        except KeyError:
            self.active_connections_map = {room_id: [websocket]}

    def disconnect(self, room_id: int, websocket: WebSocket) -> None:
        try:
            self.active_connections_map[room_id].remove(websocket)
        except Exception:
            ...

    def reset(self) -> None:
        self.active_connections_map.clear()

    async def send_to_personal(self, websocket: WebSocket, data: dict[str, Any]) -> None:
        await websocket.send_json(data=data)

    async def broadcast(self, room_id: int, data: dict[str, Any]) -> None:
        for connection in self.active_connections_map[room_id]:
            await connection.send_json(data=data)

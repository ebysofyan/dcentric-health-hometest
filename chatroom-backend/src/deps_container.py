from dependency_injector import containers, providers

from database import Database
from envs import DATABASE_URL
from repositories.chat_repository import ChatRepository
from repositories.chat_room_repository import ChatRoomRepository
from repositories.user_repository import UserRepository
from services.chat_room_service import ChatRoomService
from services.chat_service import ChatService
from services.user_service import UserService
from ws_connection_manager import ConnectionManager


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "routes.chat_room_routes",
            "routes.chat_routes",
            "routes.user_routes",
            "routes.ws_routes",
            "services.chat_room_service",
            "services.chat_service",
            "repositories.chat_room_repository",
            "repositories.chat_repository",
        ]
    )

    config = providers.Configuration()
    db = providers.Singleton(Database, database_url=DATABASE_URL)
    connection_manager = providers.Singleton(ConnectionManager)

    user_repository = providers.Factory(
        UserRepository,
        db_session=db.provided.session,
    )
    user_service = providers.Factory(UserService, user_repository=user_repository)

    chat_room_repository = providers.Factory(
        ChatRoomRepository,
        db_session=db.provided.session,
    )
    chat_room_service = providers.Factory(
        ChatRoomService,
        chat_room_repository=chat_room_repository,
    )

    chat_repository = providers.Factory(
        ChatRepository,
        db_session=db.provided.session,
    )
    chat_service = providers.Factory(ChatService, chat_repository=chat_repository)

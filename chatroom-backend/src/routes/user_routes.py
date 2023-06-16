from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from deps_container import Container
from entity.user import UserEntity
from models.chat import Chat
from services.user_service import UserService

router = APIRouter(prefix="/users")


@router.get("", response_model=list[UserEntity])
@inject
async def get_users(
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> list[Chat]:
    return user_service.get_all()

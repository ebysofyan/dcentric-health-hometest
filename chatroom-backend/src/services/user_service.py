from entity.user import CreateUserEntity
from models.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository: UserRepository = user_repository

    def get_all(self) -> list[User]:
        return self._user_repository.get_all()

    def create(self, payload: CreateUserEntity, commit: bool = True) -> User:
        try:
            return self._user_repository.create(payload=payload, commit=commit)
        except Exception as e:
            self._user_repository._db_session.rollback()
            self._user_repository._db_session.close()
            raise e

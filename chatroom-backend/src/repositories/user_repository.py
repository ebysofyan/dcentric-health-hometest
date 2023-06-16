from entity.user import CreateUserEntity
from internal.types import ScopedSession
from models.user import User


class UserRepository:
    def __init__(self, db_session: ScopedSession) -> None:
        self._db_session = db_session

    def get_all(self) -> list[User]:
        return self._db_session.query(User).all()

    def create(self, payload: CreateUserEntity, commit: bool = True) -> User:
        user = User(name=payload.name)
        self._db_session.add(user)
        if commit:
            self._db_session.commit()
        return user

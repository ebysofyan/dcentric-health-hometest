from functools import cached_property
from typing import Any

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from internal.types import ScopedSession

# engine = create_engine(envs.DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


class Database:
    def __init__(
        self, database_url: str, connect_args: dict[str, Any] = {"check_same_thread": False}
    ) -> None:
        self._database_url: str = database_url
        self._engine: Engine = create_engine(
            self._database_url, echo=True, connect_args=connect_args
        )
        self._session_factory = scoped_session(
            session_factory=sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        from models.base import Base

        Base.metadata.create_all(self._engine)

    def drop_database(self) -> None:
        from models.base import Base

        Base.metadata.drop_all(self._engine)

    @cached_property
    def session(self) -> ScopedSession:
        return self._session_factory

    # @contextmanager
    # def session(self) -> SessionFactory:
    #     session: Session = self._session_factory()
    #     try:
    #         yield session
    #     except Exception as e:
    #         logger.exception(f"Session rollback caused by: {e}")
    #         session.rollback()
    #         raise e
    #     finally:
    #         session.close()

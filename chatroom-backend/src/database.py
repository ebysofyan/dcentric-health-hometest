from functools import cached_property

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import envs
from internal.types import ScopedSession

engine = create_engine(envs.DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


class Database:
    def __init__(self) -> None:
        self._session_factory = scoped_session(
            session_factory=sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=engine,
            ),
        )

    def create_database(self) -> None:
        from models.base import Base

        Base.metadata.create_all(engine)

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

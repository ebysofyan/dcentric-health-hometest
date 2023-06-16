from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session, scoped_session

SessionFactory = Callable[..., AbstractContextManager[Session]]
ScopedSession = scoped_session

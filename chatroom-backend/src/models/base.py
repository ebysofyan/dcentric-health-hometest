import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class BaseIntPrimaryKey(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.current_timestamp()
    )

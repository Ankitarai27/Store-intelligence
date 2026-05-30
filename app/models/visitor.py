from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.store import Store
    from app.models.event import Event
    from app.models.transaction import Transaction


class Visitor(TimestampMixin, Base):
    __tablename__ = "visitors"

    __table_args__ = (
        Index("ix_visitors_store_id", "store_id"),
        Index("ix_visitors_is_staff", "is_staff"),
        Index("ix_visitors_is_converted", "is_converted"),
        Index("ix_visitors_session_start", "session_start"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    is_staff: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    session_start: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    session_end: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    is_converted: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    store: Mapped["Store"] = relationship(
        back_populates="visitors",
    )

    events: Mapped[list["Event"]] = relationship(
        back_populates="visitor",
        cascade="all, delete-orphan",
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="visitor",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"Visitor("
            f"id={self.id}, "
            f"store_id={self.store_id}, "
            f"is_staff={self.is_staff}"
            f")"
        )
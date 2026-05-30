from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from typing import Any

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.enums import EventType
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.store import Store
    from app.models.visitor import Visitor


class Event(TimestampMixin, Base):
    __tablename__ = "events"

    __table_args__ = (
        Index("ix_events_store_timestamp", "store_id", "timestamp"),
        Index("ix_events_visitor_timestamp", "visitor_id", "timestamp"),
        Index("ix_events_event_type", "event_type"),
        Index("ix_events_zone_id", "zone_id"),
        Index("ix_events_camera_id", "camera_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    visitor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("visitors.id", ondelete="CASCADE"),
        nullable=False,
    )

    store_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("stores.id", ondelete="CASCADE"),
        nullable=False,
    )

    event_type: Mapped[EventType] = mapped_column(
        String(64),
        nullable=False,
    )

    camera_id: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )

    zone_id: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    dwell_ms: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    confidence: Mapped[float] = mapped_column(
        Numeric(5, 4),
        nullable=False,
    )

    metadata_json: Mapped[dict[str, Any] | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    visitor: Mapped["Visitor"] = relationship(
        back_populates="events",
    )

    store: Mapped["Store"] = relationship(
        back_populates="events",
    )
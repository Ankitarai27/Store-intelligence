from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.visitor import Visitor


class Store(TimestampMixin, Base):
    __tablename__ = "stores"

    __table_args__ = (
        Index("ix_stores_name", "name"),
        Index("ix_stores_city", "city"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    timezone: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    visitors: Mapped[list["Visitor"]] = relationship(
        back_populates="store",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"Store("
            f"id={self.id}, "
            f"name={self.name}, "
            f"city={self.city}"
            f")"
        )
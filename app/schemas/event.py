from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import EventType


class EventIngestRequest(BaseModel):
    visitor_id: UUID
    store_id: UUID
    event_type: EventType
    camera_id: str = Field(min_length=1, max_length=128)
    zone_id: str | None = Field(default=None, max_length=128)
    timestamp: datetime
    dwell_ms: int | None = None
    confidence: Decimal
    metadata_json: dict[str, object] | None = None

    model_config = ConfigDict(from_attributes=True)


class EventIngestResponse(BaseModel):
    event_id: UUID | None
    visitor_id: UUID
    store_id: UUID
    event_type: EventType
    timestamp: datetime
    created: bool
    duplicate: bool

    model_config = ConfigDict(from_attributes=True)


class BulkEventIngestRequest(BaseModel):
    events: list[EventIngestRequest] = Field(min_length=1)

    model_config = ConfigDict(from_attributes=True)
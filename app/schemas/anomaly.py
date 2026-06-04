from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AnomalyCreate(BaseModel):
    store_id: UUID
    anomaly_type: str = Field(min_length=1, max_length=128)
    severity: str = Field(min_length=1, max_length=32)
    description: str = Field(min_length=1, max_length=1000)
    detected_at: datetime
    resolved_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class AnomalyRead(BaseModel):
    id: UUID
    store_id: UUID
    anomaly_type: str
    severity: str
    description: str
    detected_at: datetime
    resolved_at: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
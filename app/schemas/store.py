from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class StoreCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    city: str = Field(min_length=1, max_length=255)
    timezone: str = Field(min_length=1, max_length=100)

    model_config = ConfigDict(from_attributes=True)


class StoreUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    city: str | None = Field(default=None, min_length=1, max_length=255)
    timezone: str | None = Field(default=None, min_length=1, max_length=100)

    model_config = ConfigDict(from_attributes=True)


class StoreRead(BaseModel):
    id: UUID
    name: str
    city: str
    timezone: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TransactionCreate(BaseModel):
    visitor_id: UUID
    store_id: UUID
    timestamp: datetime
    basket_value: Decimal = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)


class TransactionRead(BaseModel):
    id: UUID
    visitor_id: UUID
    store_id: UUID
    timestamp: datetime
    basket_value: Decimal
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
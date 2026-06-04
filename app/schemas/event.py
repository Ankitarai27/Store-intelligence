from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional, Dict, Any
from app.models.enums import EventType

from uuid import UUID

class EventIn(BaseModel):
    event_id: UUID
    store_id: UUID
    visitor_id: UUID
    event_type: EventType
    camera_id: str
    zone_id: Optional[str] = None
    timestamp: datetime
    dwell_ms: Optional[int] = None
    confidence: Decimal
    metadata: Optional[Dict[str, Any]] = None
from __future__ import annotations

from datetime import datetime
from uuid import UUID

from app.models.enums import EventType
from app.models.visitor import Visitor
from app.repositories.visitor import VisitorRepository


class VisitorService:
    def __init__(
        self,
        repository: VisitorRepository,
    ) -> None:
        self.repository = repository

    def get(
        self,
        visitor_id: UUID,
    ) -> Visitor | None:
        return self.repository.get(visitor_id)

    def create(
        self,
        visitor: Visitor,
    ) -> Visitor:
        return self.repository.create(visitor)

    def get_active_sessions(
        self,
        store_id: UUID,
    ) -> list[Visitor]:
        return self.repository.get_active_sessions(store_id)

    def handle_session_event(
        self,
        visitor: Visitor,
        event_type: EventType,
        timestamp: datetime,
    ) -> None:
        if event_type in (
            EventType.ENTRY,
            EventType.REENTRY,
        ):
            visitor.session_start = timestamp

            if visitor.session_end is not None:
                visitor.session_end = None

        elif event_type == EventType.EXIT:
            visitor.session_end = timestamp

        self.repository.session.add(visitor)
        self.repository.session.commit()
        self.repository.session.refresh(visitor)
    def handle_session_event(
        self,
        visitor,
        event_type,
        timestamp,
    ) -> None:
        from app.models.enums import EventType

        if event_type == EventType.ENTRY:
            visitor.session_start = timestamp
            visitor.session_end = None

        elif event_type == EventType.EXIT:
            visitor.session_end = timestamp

        self.repository.session.add(visitor)
        self.repository.session.commit()
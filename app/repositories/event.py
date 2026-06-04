from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.enums import EventType
from app.models.event import Event
from app.repositories.base import BaseRepository


class EventRepository(BaseRepository[Event]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=Event)

    def create_event(self, event: Event) -> Event:
        return self.create(event)

    def get_by_visitor(self, visitor_id: UUID) -> list[Event]:
        stmt = select(Event).where(Event.visitor_id == visitor_id)

        result = self.session.execute(stmt)

        return list(result.scalars().all())

    def get_by_store(self, store_id: UUID) -> list[Event]:
        stmt = select(Event).where(Event.store_id == store_id)

        result = self.session.execute(stmt)

        return list(result.scalars().all())

    def get_by_timerange(
        self,
        store_id: UUID,
        start_ts: datetime,
        end_ts: datetime,
    ) -> list[Event]:
        stmt = (
            select(Event)
            .where(Event.store_id == store_id)
            .where(Event.timestamp >= start_ts)
            .where(Event.timestamp <= end_ts)
        )

        result = self.session.execute(stmt)

        return list(result.scalars().all())

    def exists_duplicate(
        self,
        visitor_id: UUID,
        timestamp: datetime,
        event_type: EventType,
    ) -> bool:
        stmt = (
            select(Event)
            .where(Event.visitor_id == visitor_id)
            .where(Event.timestamp == timestamp)
            .where(Event.event_type == event_type)
        )

        result = self.session.execute(stmt)

        return result.scalar_one_or_none() is not None
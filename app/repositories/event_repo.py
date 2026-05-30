from sqlalchemy.orm import Session
from app.models.event import Event
from app.repositories.base import BaseRepository


class EventRepository(BaseRepository[Event]):
    def __init__(self, session: Session):
        super().__init__(Event, session)

    def exists_duplicate(self, visitor_id, timestamp, event_type):
        return (
            self.session.query(Event)
            .filter_by(
                visitor_id=visitor_id,
                timestamp=timestamp,
                event_type=event_type,
            )
            .first()
            is not None
        )
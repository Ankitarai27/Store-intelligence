from app.schemas.event import EventIn
from app.models.event import Event
from app.models.enums import EventType


class EventService:
    def __init__(self, event_repo, visitor_service, transaction_service):
        self.event_repo = event_repo
        self.visitor_service = visitor_service
        self.transaction_service = transaction_service

    def process_event(self, event: EventIn):

        # 1. Deduplication
        if self.event_repo.exists_duplicate(
            event.visitor_id,
            event.timestamp,
            event.event_type,
        ):
            return {"status": "duplicate", "event_id": event.event_id}

        # 2. Sessionization
        visitor = self.visitor_service.get_or_create_session(
            event.visitor_id,
            event.store_id,
            event.timestamp,
        )

        if event.event_type == EventType.ENTRY:
            visitor.session_start = event.timestamp

        if event.event_type == EventType.EXIT:
            self.visitor_service.close_session(visitor, event.timestamp)

        # 3. Conversion tracking (placeholder hook)
        if event.event_type == EventType.BILLING_QUEUE_JOIN:
            pass

        # 4. Persist event
        db_event = Event(
            id=event.event_id,
            visitor_id=event.visitor_id,
            store_id=event.store_id,
            event_type=event.event_type,
            camera_id=event.camera_id,
            zone_id=event.zone_id,
            timestamp=event.timestamp,
            dwell_ms=event.dwell_ms,
            confidence=event.confidence,
            metadata_json=event.metadata,
        )

        self.event_repo.add(db_event)
        self.event_repo.commit()

        return {
            "status": "processed",
            "event_id": event.event_id,
        }
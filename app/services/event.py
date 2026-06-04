from app.models.event import Event
from app.models.enums import EventType
from app.repositories.event import EventRepository
from app.services.transaction import TransactionService
from app.services.visitor import VisitorService
from app.schemas.event import EventIngestRequest


class EventService:
    def __init__(
        self,
        repository: EventRepository,
        visitor_service: VisitorService,
        transaction_service: TransactionService,
    ) -> None:
        self.repository = repository
        self.visitor_service = visitor_service
        self.transaction_service = transaction_service

    def process_event(self, event: EventIngestRequest) -> dict:

        duplicate = self.repository.exists_duplicate(
            visitor_id=event.visitor_id,
            timestamp=event.timestamp,
            event_type=event.event_type,
        )

        if duplicate:
            return {
                "status": "duplicate",
                "event_id": None,
            }

        created = self.repository.create_event(event)

        visitor = self.visitor_service.get(event.visitor_id)

        if visitor is not None:
            self.visitor_service.handle_session_event(
                visitor,
                event.event_type,
                event.timestamp,
            )

        return {
            "status": "processed",
            "event_id": str(created.id),
        }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.schemas.event import EventIngestRequest, EventIngestResponse
from app.models.event import Event

from app.repositories.event import EventRepository
from app.repositories.visitor import VisitorRepository
from app.repositories.transaction import TransactionRepository

from app.services.event import EventService
from app.services.visitor import VisitorService
from app.services.transaction import TransactionService

router = APIRouter()


@router.post("/events/ingest", response_model=EventIngestResponse)
def ingest_event(
    event: EventIngestRequest,
    session: Session = Depends(get_session),
):
    event_repo = EventRepository(session)
    visitor_repo = VisitorRepository(session)
    transaction_repo = TransactionRepository(session)

    visitor_service = VisitorService(visitor_repo)
    transaction_service = TransactionService(transaction_repo)

    service = EventService(
        event_repo,
        visitor_service,
        transaction_service,
    )

    db_event = Event(
        visitor_id=event.visitor_id,
        store_id=event.store_id,
        event_type=event.event_type,
        camera_id=event.camera_id,
        zone_id=event.zone_id,
        timestamp=event.timestamp,
        dwell_ms=event.dwell_ms,
        confidence=event.confidence,
        metadata_json=event.metadata_json,
    )

    result = service.process_event(db_event)

    return EventIngestResponse(
        event_id=result.get("event_id"),
        visitor_id=event.visitor_id,
        store_id=event.store_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        created=not result.get("status") == "duplicate",
        duplicate=result.get("status") == "duplicate",
    )
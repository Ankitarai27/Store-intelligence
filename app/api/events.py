from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.event import EventIn
from app.db.session import get_session

from app.repositories.event_repo import EventRepository
from app.repositories.visitor_repo import VisitorRepository
from app.repositories.transaction_repo import TransactionRepository

from app.services.event_service import EventService
from app.services.visitor_service import VisitorService
from app.services.transaction_service import TransactionService

router = APIRouter()


@router.post("/events/ingest")
def ingest_event(event: EventIn, session: Session = Depends(get_session)):

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

    result = service.process_event(event)

    return result
from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.repositories.store import StoreRepository
from app.repositories.visitor import VisitorRepository
from app.repositories.event import EventRepository
from app.repositories.transaction import TransactionRepository
from app.repositories.anomaly import AnomalyRepository

from app.services.store import StoreService
from app.services.visitor import VisitorService
from app.services.event import EventService
from app.services.transaction import TransactionService
from app.services.anomaly import AnomalyService
from app.services.visitor import VisitorService

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_store_repository(
    db: Session = Depends(get_db),
) -> StoreRepository:
    return StoreRepository(db)


def get_visitor_repository(
    db: Session = Depends(get_db),
) -> VisitorRepository:
    return VisitorRepository(db)


def get_event_repository(
    db: Session = Depends(get_db),
) -> EventRepository:
    return EventRepository(db)


def get_transaction_repository(
    db: Session = Depends(get_db),
) -> TransactionRepository:
    return TransactionRepository(db)


def get_anomaly_repository(
    db: Session = Depends(get_db),
) -> AnomalyRepository:
    return AnomalyRepository(db)


def get_store_service(
    repository: StoreRepository = Depends(get_store_repository),
) -> StoreService:
    return StoreService(repository)


def get_visitor_service(
    repository: VisitorRepository = Depends(get_visitor_repository),
) -> VisitorService:
    return VisitorService(repository)


def get_transaction_service(
    repository: TransactionRepository = Depends(
        get_transaction_repository,
    ),
) -> TransactionService:
    return TransactionService(repository)


def get_anomaly_service(
    repository: AnomalyRepository = Depends(
        get_anomaly_repository,
    ),
) -> AnomalyService:
    return AnomalyService(repository)


def get_event_service(
    event_repository: EventRepository = Depends(
        get_event_repository,
    ),
    visitor_service: VisitorService = Depends(
        get_visitor_service,
    ),
    transaction_service: TransactionService = Depends(
        get_transaction_service,
    ),
) -> EventService:
    return EventService(
        event_repository,
        visitor_service,
        transaction_service,
    )
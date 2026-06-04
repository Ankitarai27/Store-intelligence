from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.api.deps import get_transaction_service
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from app.schemas.transaction import TransactionRead
from app.services.transaction import TransactionService

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post(
    "",
    response_model=TransactionRead,
)
def create_transaction(
    payload: TransactionCreate,
    service: TransactionService = Depends(
        get_transaction_service,
    ),
) -> Transaction:
    transaction = Transaction(
        visitor_id=payload.visitor_id,
        store_id=payload.store_id,
        timestamp=payload.timestamp,
        basket_value=payload.basket_value,
    )

    return service.create(transaction)


@router.get(
    "",
    response_model=list[TransactionRead],
)
def list_transactions(
    store_id: UUID,
    service: TransactionService = Depends(
        get_transaction_service,
    ),
) -> list[Transaction]:
    return service.get_by_store(store_id)
from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.base import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=Transaction)

    def create_transaction(self, transaction: Transaction) -> Transaction:
        return self.create(transaction)

    def get_by_store(self, store_id: UUID) -> list[Transaction]:
        stmt = select(Transaction).where(Transaction.store_id == store_id)

        result = self.session.execute(stmt)

        return list(result.scalars().all())

    def get_by_visitor(self, visitor_id: UUID) -> list[Transaction]:
        stmt = select(Transaction).where(Transaction.visitor_id == visitor_id)

        result = self.session.execute(stmt)

        return list(result.scalars().all())
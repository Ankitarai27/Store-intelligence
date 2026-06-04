from uuid import UUID

from app.models.transaction import Transaction
from app.models.visitor import Visitor
from app.repositories.transaction import TransactionRepository


class TransactionService:
    def __init__(
        self,
        repository: TransactionRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        transaction: Transaction,
        visitor: Visitor | None = None,
    ) -> Transaction:

        result = self.repository.create_transaction(
            transaction,
        )

        if visitor is not None:
            visitor.is_converted = True
            self.repository.session.commit()

        return result

    def get_by_store(
        self,
        store_id: UUID,
    ) -> list[Transaction]:
        return self.repository.get_by_store(store_id)

    def get_by_visitor(
        self,
        visitor_id: UUID,
    ) -> list[Transaction]:
        return self.repository.get_by_visitor(visitor_id)
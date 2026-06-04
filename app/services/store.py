from uuid import UUID

from app.models.store import Store
from app.repositories.store import StoreRepository


class StoreService:
    def __init__(
        self,
        repository: StoreRepository,
    ) -> None:
        self.repository = repository

    def create(self, store: Store) -> Store:
        return self.repository.create(store)

    def get(self, store_id: UUID) -> Store | None:
        return self.repository.get(store_id)

    def list(self) -> list[Store]:
        return self.repository.list()

    def get_by_name(self, name: str) -> Store | None:
        return self.repository.get_by_name(name)
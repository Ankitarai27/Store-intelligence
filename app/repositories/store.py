from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.store import Store
from app.repositories.base import BaseRepository


class StoreRepository(BaseRepository[Store]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=Store)

    def get_by_name(self, name: str) -> Store | None:
        stmt = select(Store).where(Store.name == name)

        result = self.session.execute(stmt)

        return result.scalar_one_or_none()